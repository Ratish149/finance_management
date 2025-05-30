from django.db import models
from authentication.models import Organization, CustomUser
# Create your models here.


class FinanceRecord(models.Model):
    TRANSACTION_TYPE = [
        ('RECEIVED', 'Received'),
        ('PAID', 'Paid'),
    ]
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount}'
