from .models import *
import django_filters


class VedeoFilter(django_filters.FilterSet):
    class Meta:
        model = Video
        fields = ['caption', 'date']

    