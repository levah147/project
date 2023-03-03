from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY =(
    ('food', 'food'),
    ('cars','cars'),
    ('fans','fans'),
)
class product(models.Model):
    name = models.CharField(max_length=100 ,null=True)
    category = models.CharField(max_length=20 , choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)

    class meta:
        verbose_name_plural = 'staff Product'

    def __str__(self):
        return f'{self.name} -{self.quantity}'
    
class order(models.Model):
    product =models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    staff =models.ForeignKey(User,models.CASCADE, null=True)
    order_category = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'