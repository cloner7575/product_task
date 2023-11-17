from rest_framework import serializers
from .models import Product, Variety, AvailabilitySize, VarietyImage, Category, Brand


class AvailabilitySizeSerializer(serializers.ModelSerializer):
    """
    Serializer for the AvailabilitySize model.
    """

    class Meta:
        model = AvailabilitySize
        fields = ['size_type', 'price', 'count', 'discount']


class VarietyImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the VarietyImage model.
    """

    class Meta:
        model = VarietyImage
        fields = ['url']


class VarietySerializer(serializers.ModelSerializer):
    """
    Serializer for the Variety model.
    Includes nested serializers for AvailabilitySize and VarietyImage.
    """
    available_sizes = AvailabilitySizeSerializer(many=True)
    images = VarietyImageSerializer(many=True)

    class Meta:
        model = Variety
        fields = ['id', 'color', 'available_sizes', 'images']


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    """

    class Meta:
        model = Category
        fields = ['name']


class BrandSerializer(serializers.ModelSerializer):
    """
    Serializer for the Brand model.
    """

    class Meta:
        model = Brand
        fields = ['name']


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.
    Includes nested serializers for Variety, and character fields for brand and category.
    """
    variety = VarietySerializer(many=True)
    brand = serializers.CharField(source='brand.name')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = ['name', 'brand', 'category', 'features', 'variety']

    def create(self, validated_data):
        """
        Overrides the default create method.
        Uses the _save_product method to create a new product instance.
        """
        return self._save_product(validated_data)

    def update(self, instance, validated_data):
        """
        Overrides the default update method.
        Uses the _save_product method to update an existing product instance.
        """
        return self._save_product(validated_data, instance)

    def _save_product(self, validated_data, instance=None):
        """
        A helper method to create or update a product instance.
        This method reduces the number of database queries and code duplication.
        """
        brand_data = validated_data.pop('brand')
        category_data = validated_data.pop('category')
        variety_data = validated_data.pop('variety')

        brand, _ = Brand.objects.get_or_create(name=brand_data['name'])
        category, _ = Category.objects.get_or_create(name=category_data['name'])

        if instance is None:
            product = Product.objects.create(brand=brand, category=category, **validated_data)
        else:
            product = instance
            product.name = validated_data.get('name', instance.name)
            product.brand = brand
            product.category = category
            product.features = validated_data.get('features', instance.features)
            product.save()
            product.variety.clear()

        sizes = AvailabilitySize.objects.all()
        images = VarietyImage.objects.all()

        for variety_item in variety_data:
            variety, created = Variety.objects.get_or_create(color=variety_item['color'])
            if created:
                sizes_data = variety_item.pop('available_sizes')
                for size_data in sizes_data:
                    size, created = sizes.get_or_create(**size_data)
                    if created:
                        size.save()
                    variety.available_sizes.add(size)
                image_data = variety_item.pop('images')
                for image in image_data:
                    image, created = images.get_or_create(**image)
                    if created:
                        image.save()
                    variety.images.add(image)

            product.variety.add(variety)

        return product
