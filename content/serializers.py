from rest_framework import serializers
from .models import (
    Category,
    Product,
    ProductVariant,
    JobRole,
    OurStoryVideo,
    OurMissionVideo
)


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "image", "is_active"]

    def get_image(self, obj):
        if obj.image:
            request = self.context.get("request")
            url = obj.image.url
            return request.build_absolute_uri(obj.image.url) if request else url
        return None


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # READ
    category = CategorySerializer(read_only=True)
    variants = ProductVariantSerializer(many=True, read_only=True)

    # WRITE
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    variant_ids = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all(),
        many=True,
        source="variants",
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "size",
            "image",
            "product_type",
            "is_active",
            "is_best_seller",
            "rating",
            "category",
            "category_id",
            "variants",
            "variant_ids",
        ]


class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobRole
        fields = '__all__'


class OurStoryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStoryVideo
        fields = ['id', 'youtube_url']


class OurMissionVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMissionVideo
        fields = ['id', 'youtube_url']
