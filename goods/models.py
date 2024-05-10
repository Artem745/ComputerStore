from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to="categories_images", blank=True, null=True)
    parent_category = models.ForeignKey('self', related_name='sub_categories', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "category"
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ("id",)


    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=0)
    discount = models.DecimalField(default=0, max_digits=3, decimal_places=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    removebg = models.BooleanField(default=False)

    class Meta:
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"
        ordering = ("id",)

    def __str__(self):
        return f"{self.name}, quantity: {self.quantity}"

    def display_id(self):
        return f"{self.id:05}"

    def discount_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 0)
        return self.price

    def removebg_image(self):
        from goods.utils import removebg

        if self.image:
            removebg(old_image_path=f"media/{self.image.name}")


@receiver(post_save, sender=Products)
def process_product_image(sender, instance, **kwargs):
    if instance.image and instance.removebg:
        instance.removebg_image()