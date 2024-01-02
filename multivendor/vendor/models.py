from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields related to the seller profile if needed
    # For example: seller_name, seller_location, etc.

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_file = models.FileField(upload_to='product_files/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)  # Add this line to associate with Seller

    def __str__(self):
        return self.name

    
    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])
