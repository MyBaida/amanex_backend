from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/', default='categories/default.png', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
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
    image = models.ImageField(upload_to='products/', default='products/default.png', blank=True)
    variants = models.ManyToManyField(
        ProductVariant,
        related_name='products',
        blank=True
    )
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

    def __str__(self):
        return self.name


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

