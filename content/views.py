from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


from .models import (
    Category,
    Product,
    JobRole,
    OurStoryVideo,
    OurMissionVideo, 
    ProductVariant
)

from .serializers import (
    CategorySerializer,
    ProductSerializer,
    JobRoleSerializer,
    OurStoryVideoSerializer,
    OurMissionVideoSerializer,
    ProductVariantSerializer
)


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {"detail": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def category_update(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {"detail": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = CategorySerializer(
        category,
        data=request.data,
        partial=True  
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def category_delete(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {"detail": "Category not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    category.delete()
    return Response(
        {"detail": "Category deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def product_list_by_category(request, category_id):
    products = Product.objects.filter(
        category_id=category_id
    )
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def product_update(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductSerializer(
        product,
        data=request.data,
        partial=True  # allows updating only some fields
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def product_delete(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    product.delete()
    return Response(
        {"detail": "Product deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(["GET"])
def best_seller_products(request):
    products = Product.objects.filter(
        is_best_seller=True
    )
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def variant_list(request):
    variants = ProductVariant.objects.all()
    serializer = ProductVariantSerializer(variants, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def product_variant_create(request):
    serializer = ProductVariantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(["GET"])
def product_variant_detail(request, pk):
    try:
        variant = ProductVariant.objects.get(pk=pk)
    except ProductVariant.DoesNotExist:
        return Response(
            {"detail": "Variant not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductVariantSerializer(variant)
    return Response(serializer.data)


@api_view(['PUT'])
def product_variant_update(request, pk):
    try:
        variant = ProductVariant.objects.get(pk=pk)
    except ProductVariant.DoesNotExist:
        return Response(
            {"detail": "Variant not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = ProductVariantSerializer(
        variant,
        data=request.data,
        partial=True  
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def product_variant_delete(request, pk):
    try:
        variant = ProductVariant.objects.get(pk=pk)
    except ProductVariant.DoesNotExist:
        return Response(
            {"detail": "Variant not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    variant.delete()
    return Response(
        {"detail": "Variant deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET'])
def job_list(request):
    jobs = JobRole.objects.all()
    serializer = JobRoleSerializer(jobs, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def job_detail(request, pk):
    try:
        job = JobRole.objects.get(pk=pk)
    except JobRole.DoesNotExist:
        return Response(
            {"detail": "Job role not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = JobRoleSerializer(job)
    return Response(serializer.data)


@api_view(['POST'])
def job_create(request):
    serializer = JobRoleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["PATCH"])
def toggle_job(request, pk):
    try:
        job = JobRole.objects.get(pk=pk)
    except JobRole.DoesNotExist:
        return Response(
            {"detail": "Job role not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    job.is_open = not job.is_open
    job.save()
    return Response({"is_open": job.is_open})


@api_view(['PUT'])
def job_update(request, pk):
    try:
        job = JobRole.objects.get(pk=pk)
    except JobRole.DoesNotExist:
        return Response(
            {"detail": "Job role not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = JobRoleSerializer(
        job,
        data=request.data,
        partial=True
    )

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def job_delete(request, pk):
    try:
        job = JobRole.objects.get(pk=pk)
    except JobRole.DoesNotExist:
        return Response(
            {"detail": "Job role not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    job.delete()
    return Response(
        {"detail": "Job role deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET'])
def our_story_video(request):
    video = OurStoryVideo.objects.first()
    if not video:
        return Response({"youtube_url": ""})
    serializer = OurStoryVideoSerializer(video)
    return Response(serializer.data)


@api_view(['POST'])
def update_our_story_video(request):
    video, created = OurStoryVideo.objects.get_or_create(id=1)
    serializer = OurStoryVideoSerializer(video, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def our_mission_video(request):
    video = OurMissionVideo.objects.first()
    if not video:
        return Response({"youtube_url": ""})
    serializer = OurMissionVideoSerializer(video)
    return Response(serializer.data)


@api_view(['POST'])
def update_our_mission_video(request):
    video, created = OurMissionVideo.objects.get_or_create(id=1)
    serializer = OurMissionVideoSerializer(video, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
