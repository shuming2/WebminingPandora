from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination, _positive_int
from rest_framework.response import Response


class ProductPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = "size"

    def get_paginated_response(self, data):
        response = OrderedDict([
            ("query", "posts"),
            ("count", self.page.paginator.count),
            ("size", self.page_size),
            ("next", self.get_next_link()),
            ("previous", self.get_previous_link()),
            ("products", data)
        ])
        if not response["next"]:
            response.pop("next")
        if not response["previous"]:
            response.pop("previous")
        return Response(response)

    def get_page_size(self, request):
        if self.page_size_query_param:
            try:
                self.page_size =  _positive_int(
                    request.query_params[self.page_size_query_param],
                    strict=True,
                    cutoff=self.max_page_size
                )
            except (KeyError, ValueError):
                pass

        return self.page_size