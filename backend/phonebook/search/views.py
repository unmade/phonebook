# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

from rest_framework.response import Response
from rest_framework.views import APIView

from .doctypes import EmployeeIndex
from .serializers import SuggestSerializer


class Suggests(APIView):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')

        results = (
            EmployeeIndex
            .search()
            .suggest(
                name='name_suggestions',
                text=query,
                completion={
                    'field': 'suggest',
                    'size': 3,
                    'fuzzy': {
                        'fuzziness': 1,
                    },
                },
            )
        )

        serializer = SuggestSerializer(
            results.execute().suggest.name_suggestions[0].options,
            many=True,
        )

        return Response(serializer.data)
