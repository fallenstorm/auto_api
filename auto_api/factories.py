import django.apps
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers
from auto_api.pagination import AutoApiPagination


class ViewSetFactory:
    """
    Class, generated viewset, using all django models, excluding system(django.contrib)
    """
    viewsets_dict = {}

    @classmethod
    def build_serializer(cls, model):
        """
        Generates serializer for 1 model class
        :param model: model class
        :return:
        """
        serializer_meta_class = type(f'{model.__name__}Meta', (), {
            'model': model,
            'fields': '__all__'
        })

        serializer_class = type(f'{model.__name__}Serializer', (serializers.ModelSerializer,), {
            'Meta': serializer_meta_class
        })

        return serializer_class

    @classmethod
    def build_viewset(cls, model, serializer):
        """
        Generates viewset for 1 model class
        :param model:
        :param serializer:
        :return:
        """
        opts = model._meta

        filter_fields = [
            f.name for f in sorted(opts.fields + opts.many_to_many)
            if not (getattr(f.remote_field, 'parent_link', False))
        ]

        return type(f'{model.__name__}ViewSet', (viewsets.ModelViewSet,), {
            'queryset': model.objects.all(),
            'serializer_class': serializer,
            'pagination_class': AutoApiPagination,
            'filter_backends': [DjangoFilterBackend, filters.OrderingFilter],
            'filterset_fields': filter_fields,
            'ordering_fields': '__all__'
        })

    @classmethod
    def get_viewsets(cls, *args, **kwargs):
        """
        Generates dict like {'model_name': viewset_class, ...} for all models in django apps,
        excluding django.contrib
        :param args:
        :param kwargs:
        :return:
        """
        models = kwargs.get('models', django.apps.apps.get_models())
        for model in models:
            if 'django.contrib' in model.__module__ or model.__name__ in cls.viewsets_dict:
                continue
            else:
                serializer_class = cls.build_serializer(model)
                viewset_class = cls.build_viewset(model, serializer_class)

                cls.viewsets_dict[model.__name__] = viewset_class

        return cls.viewsets_dict