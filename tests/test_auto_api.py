from django.test import TestCase
from .models import Blog, Post, Smi
from auto_api.factories import ViewSetFactory


class TestAutoApi(TestCase):
    def setUp(self):
        pass

    def test_one(self):
        serializer_class = ViewSetFactory.build_serializer(Blog)

        assert serializer_class.__name__ == 'BlogSerializer'
        assert serializer_class.Meta.model == Blog
        assert serializer_class.Meta.fields == '__all__'

        viewset_class = ViewSetFactory.build_viewset(Blog, serializer_class)

        assert str(viewset_class.queryset.query) == 'SELECT "tests_blog"."id", "tests_blog"."created_at", ' \
                                                    '"tests_blog"."name", "tests_blog"."subscribers" FROM "tests_blog"'
        assert viewset_class.serializer_class == serializer_class
        assert set(viewset_class.filterset_fields) == {'id', 'created_at', 'name', 'subscribers', 'smi'}
        assert viewset_class.ordering_fields == '__all__'

    def test_all(self):
        viewset_dict = ViewSetFactory.get_viewsets(models=(Blog, Post, Smi))
        assert len(viewset_dict) == 3
        assert set(viewset_dict.keys()) == {'Blog', 'Post', 'Smi'}
