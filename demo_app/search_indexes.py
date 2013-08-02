from haystack import indexes
from .models import Property


class PropertiesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    value = indexes.CharField(model_attr='value')
    product = indexes.CharField(model_attr='product')

    def get_model(self):
        return Property

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
