from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False,
                                     blank=False, default=name)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Pack(models.Model):
    sku = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254)
    description = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    on_sale = models.BooleanField(default=False)
    reduced_price = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sales = models.IntegerField(null=False, blank=False, default='0',
                                editable=False)
    image = models.ImageField(null=False, blank=True)
    sample_track = models.FileField(null=False, blank=True)
    download_file = models.FileField(null=False, blank=False, default='.')

    def __str__(self):
        return self.name
