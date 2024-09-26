from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nationality = models.CharField(max_length=100)

    class Meta:
        db_table = 'custom_brand_table'
        ordering = ['id']  

    def __str__(self):
        return self.name

class Phone(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    status_choices = [
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE', 'Unavailable')
    ]
    status = models.CharField(max_length=11, choices=status_choices, default='AVAILABLE')
    manufacturer_country = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'custom_phone_table'
        unique_together = ('brand', 'model', 'color')
        ordering = ['id']

    def save(self, *args, **kwargs):
        self.model = f"{self.model} {self.color}"
        if self.quantity == 0:
            self.status = 'UNAVAILABLE'
        else:
            self.status = 'AVAILABLE'
        super(Phone, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand.name} {self.model}"
