from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ProductPagination(PageNumberPagination):

    page_size = 5
    # Número de objetos que se devuelven por página.

    page_size_query_param = "size"
    # Permite que el cliente indique cuántos resultados quiere.
    # Ejemplo: /api/products/?size=25

    max_page_size = 100
    # Límite máximo permitido cuando el cliente usa ?size=

    page_query_param = "pagina"
    # Cambia el nombre del parámetro para navegar entre páginas.
    # Por defecto es ?page=2
    # Ahora sería ?pagina=2

    last_page_strings = ("ultima",)
    # Cambia la palabra reservada "last".
    # Ahora sería ?pagina=ultima


    def get_paginated_response(self, data):
        return Response({
            "success": True,
            "total": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
        })