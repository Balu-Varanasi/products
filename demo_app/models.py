from django.db import models
from django.utils.translation import ugettext_lazy as _


class Property(models.Model):
    product = models.ForeignKey("Product",
                                related_name='product_properties')
    name = models.CharField(verbose_name=u'Name of the Property',
                            max_length=128)
    value = models.CharField(verbose_name=u'Value of the Property',
                             max_length=256)

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')

    def __unicode__(self):
        return "%s %s" % (self.product.name, self.name)


class Product(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __unicode__(self):
        return self.name
