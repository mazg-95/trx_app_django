"""
    Module with app models
"""

import uuid
from django.db import models

class Company(models.Model):
    """ Class representing the sellers """
    name = models.CharField(max_length=250, null=False)
    status = models.BooleanField(null=False)

class Customer(models.Model):
    """
        Class representing a Customer Benefits Card Holder
    """
    name = models.CharField(max_length=250, null=False)

class BenefitsCard(models.Model):
    """
        Benefits Card Class
    """
    card_id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, editable=False)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False)
    credit = models.DecimalField(max_digits=20, decimal_places= 6, null=False)

class Transaction(models.Model):
    """ Class representing a transaction made by a Card Holder """

    TRX_STATUS = (('closed', 'closed'), ('reversed', 'reversed'), ('pending', 'pending'))

    trx_id = models.UUIDField(primary_key=True, null=False, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, on_delete=models.PROTECT)
    card_id = models.ForeignKey(BenefitsCard, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=20, decimal_places= 6, null=False)
    transaction_date = models.DateTimeField(null=False)
    paid_date = models.DateTimeField()
    transaction_status = models.CharField(choices=TRX_STATUS, max_length=8, null=False)
    approvement_status = models.BooleanField(null=False, default=False)
    paid = models.BooleanField(null=False, default=False)
    