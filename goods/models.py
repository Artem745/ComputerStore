from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = "category"
        verbose_name= "category"
        verbose_name_plural= "categories"



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

    class Meta:
        db_table = "product"
        verbose_name= "product"
        verbose_name_plural= "products"

    def __str__(self):
        return f'{self.name}, quantity: {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'

    def discount_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 0)
        return self.price