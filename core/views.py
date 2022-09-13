from django.shortcuts import render

# we only want to display the data. Thus, we're importing JsonResponse
from django.http import JsonResponse

# 3rd party imports
from rest_framework.response import Response
from rest_framework.views import APIView



#! 3rd party DRF
class TestView(APIView):
    def get (self, request, *args, **kwargs):
        data = {
        'name': 'john',
        'age': 23
        }

        return Response(data)






#! built-in django api
# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }

#     return JsonResponse(data) # since we are passing a dictionary we just pass data as an argument, but if we were to pass a list we'd do it by passing (data, safe=False)

