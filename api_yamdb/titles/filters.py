from django_filters import rest_framework as filters

from titles.models import Title


class TitleFilter(filters.FilterSet):
    """Фильтр для названий."""

    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:

        model = Title
        fields = ['genre', 'category', 'name', 'year']
