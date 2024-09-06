from rest_framework import pagination

class Pagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_params = 'pagina'