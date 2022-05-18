from django.db import models


class Classification(models.Model):
    """ classification model """
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ product model with foreign key link to classification model """
    # if a 'classification' is deleted, set any products that use it to null
    classification = models.ForeignKey('Classification', null=True, blank=True,
                                       on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, null=True, blank=True)
    bike_model = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    price_now = models.DecimalField(max_digits=6, decimal_places=2,
                                    null=False, blank=False,
                                    editable=False)
    price_was = models.DecimalField(max_digits=6, decimal_places=2,
                                    null=True, blank=True,
                                    editable=False)
    # price_now = models.IntegerField()
    # price_was = models.IntegerField(null=True, blank=True)
    brand = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100)
    sizes = models.BooleanField(default=False, null=True, blank=True)
    discipline = models.CharField(max_length=100, null=True)
    material = models.CharField(max_length=100, null=True)
    wheel_size = models.CharField(max_length=30, null=True)
    rear_derailleur = models.CharField(max_length=100, null=True)
    colour = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=30, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    frame_in_inches = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.bike_model
