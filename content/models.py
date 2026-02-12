from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary_storage.storage import MediaCloudinaryStorage

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', null=True, blank=True, storage=MediaCloudinaryStorage())
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class VariantType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    size = models.CharField(max_length=50)  # e.g. 250ml
    image = models.ImageField(upload_to='products/', storage=MediaCloudinaryStorage(), default='products/default.png', blank=True)

    product_type = models.CharField( max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_best_seller = models.BooleanField(default=False)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
        null=True,
        blank=True
    )
    variant_type = models.ForeignKey(
        VariantType,
        related_name='product_variants',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='product_variants/',
        storage=MediaCloudinaryStorage(),
        null=True,
        blank=True
    )

    class Meta:
        unique_together = ('product', 'variant_type')

    def __str__(self):
        product_name = self.product.name if self.product else "No Product"
        variant_name = self.variant_type.name if self.variant_type else "No Variant"
        return f"{product_name} - {variant_name}"



class OurStoryVideo(models.Model):
    youtube_url = models.URLField()

    def __str__(self):
        return "Our Story Video"


class OurMissionVideo(models.Model):
    youtube_url = models.URLField()

    def __str__(self):
        return "Our Mission Video"


class JobRole(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
    ]

    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES
    )

    experience = models.CharField(max_length=50)

    description = models.TextField()

    requirements = models.TextField(
        help_text="One requirement per line"
    )
    responsibilities = models.TextField(
        help_text="One responsibility per line"
    )
    is_open = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

