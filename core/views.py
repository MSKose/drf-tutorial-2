from django.shortcuts import render

# we only want to display the data. Thus, we're importing JsonResponse (for native django api, not DRF)
from django.http import JsonResponse

# 3rd party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

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

#! CBV DRF views
class PostView(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    serializer_class = PostSerializer
    queryset = Post.objects.all()


    '''
    The following functions get and post are by default defined already in generics.ListAPIView (for get) and generics.CreateAPIView (for post). 
    Using mixins, we can also combine them both in one class like this one (PostView). For the sake of education we will define a class named
    PostCreateView to see how simple it'd be to inherit the already written get method for it
    '''

    def get (self, request, *args, **kwargs): # without defining this we'd get an "detail": "Method \"GET\" not allowed." error from DRF
        return self.list(request, *args, **kwargs) # we have checked this one from the ListModelMixin mixin and adjusted it to our liking

    def post (self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # we have checked this one from the CreateModelMixin mixin and adjusted it to our liking


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer # we are at least required to specify serializer_class and queryset
    queryset = Post.objects.all()

    '''
    And that's it. By only defining serializer_class and queryset we have defined (inherited) a post class. Click on the CreateAPIView and 
    see it for your self how similar the method is with the hand-writtten post method above in PostView class. And remember we could still 
    add get method functionality to this class with the mixins.ListModelMixin mixin but then again we'd then need to add the get function
    by ourselves. But, there's an even better generics views ListCreateAPIView which combines get and post in a class. More below:
    '''

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer # remember, we are required to at least specify serializer_class and queryset
    queryset = Post.objects.all()


    '''
    And that's all we had to define. This class based view handles both get and post method. Let's head to urls.py and call this view and 
    see that it is indeed giving the same result as the PostView view
    '''




#! FBV DRF views
# class TestView(APIView):

#     permission_classes = [IsAuthenticated] # permission_classes is a class based view DRF attribute. And it takes a list or a tuple 


#     def get (self, request, *args, **kwargs):
#         # data = {
#         # 'name': 'john',
#         # 'age': 23
#         # }
#         # return Response(data)
#         queryset = Post.objects.all()

#         # serializing multiple instances:
#         # serializer = PostSerializer(queryset, many=True) # many=True since we're passing many instances

#         # serializing one instance:
#         post = queryset.first()
#         serializer = PostSerializer(post)

#         return Response(serializer.data)


#     def post (self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid(): # let's check if it's valid
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)