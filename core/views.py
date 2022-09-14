from django.shortcuts import render

# we only want to display the data. Thus, we're importing JsonResponse (for native django api, not DRF)
from django.http import JsonResponse

# 3rd party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post


#! built-in django api
# def test_view(request):
#     data = {
#         'name': 'john',
#         'age': 23
#     }

#     return JsonResponse(data) # since we are passing a dictionary we just pass data as an argument, but if we were to pass a list we'd do it by passing (data, safe=False)


#! 3rd party DRF
class TestView(APIView):

    permission_classes = [IsAuthenticated] # permission_classes is a class based view DRF attribute. And it takes a list or a tuple 


    def get (self, request, *args, **kwargs):
        # data = {
        # 'name': 'john',
        # 'age': 23
        # }
        # return Response(data)
        queryset = Post.objects.all()

        # serializing multiple instances:
        # serializer = PostSerializer(queryset, many=True) # many=True since we're passing many instances

        # serializing one instance:
        post = queryset.first()
        serializer = PostSerializer(post)

        return Response(serializer.data)


    def post (self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): # let's check if it's valid
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)