from haystack import indexes
from .models import Product


class PropertiesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    product = indexes.CharField(model_attr='product')
    name = indexes.CharField(model_attr='name')
    value = indexes.CharField(model_attr='value')

    def get_model(self):
        return Product

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
