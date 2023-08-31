from django.db import models

# Create your models here.
class CustomerData(models.Model):
    customer_id = models.CharField(max_length=100)
    combined_data=models.TextField(max_length=500)

    def __str__(self):
        return f"CustomerData(customer_id={self.customer_id})"

