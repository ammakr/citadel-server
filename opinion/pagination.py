from rest_framework.pagination import PageNumberPagination


class OpinionPagination(PageNumberPagination):
    page_size = 5
