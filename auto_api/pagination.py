from rest_framework.pagination import PageNumberPagination


class AutoApiPagination(PageNumberPagination):
    """
    Simple pagination class with 1 attribute changed
    """
    page_size_query_param = 'limit'
