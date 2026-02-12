from rest_framework import serializers
from .models import (
    Category,
    Product,
    ProductVariant,
    JobRole,
    OurStoryVideo,
    VariantType,
    OurMissionVideo
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class VariantTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantType
        fields = ["id", "name"]



class ProductVariantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="variant_type.name")
    # variant_type = VariantTypeSerializer(read_only=True)
    variant_type_id = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        source="variant_type"
    )

    class Meta:
        model = ProductVariant
        fields = ["id", "name", "variant_type_id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    variants = ProductVariantSerializer(
        many=True,
        read_only=True
    )

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
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
