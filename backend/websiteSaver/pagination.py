from rest_framework import pagination


class SitePagination(pagination.CursorPagination):
    page_size = 10
    ordering = 'id'
    


class TagPagination(pagination.CursorPagination):
    page_size = 20
    ordering = 'id'