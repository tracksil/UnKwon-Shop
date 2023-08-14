from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    class Meta:
        app_label = "products"
        db_table = "products"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.sku:
            self.generate_code()

    def generate_code(self):
        str_id = str(self.id)
        prefix = "PR"
        digits_len = 12 - len(prefix)
        self.sku = f"{prefix}{str(str_id).zfill(digits_len)}"
        self.save()
