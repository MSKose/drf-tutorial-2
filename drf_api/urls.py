from django.contrib import admin
from django.urls import path, include
from core.views import (
    # test_view, 
    # TestView,
    PostView, 
    PostListCreateView,
    )


# what this basically does is, when username and password correctly passes, it provide with the api token key
from rest_framework.authtoken.views import obtain_auth_token

# there are also 3rd party authentication configuration packages DRF recommends: https://www.django-rest-framework.org/api-guide/authentication/#third-party-packages
# I picked dj-rest-auth from there. The docs for that: https://github.com/iMerica/dj-rest-auth


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', test_view, name='test'),
    # path('', TestView.as_view(), name='test'),
    path('', PostView.as_view(), name='test'),
    path('get-and-post/', PostListCreateView.as_view(), name='get-and-post'), # defining this url to see if we get the same result with the above url 


    # head over to api/token in Postman, to the url part select POST and type http://127.0.0.1:8000/api/token/ (cuz that's what we provided here) 
    # and as for the tab select body/form-data and as key-value pairs pass 'username' as key and your username as value and 'password' as key and 
    # your password as value. Then hit send and, boom, you'll be seeing your token key sent as an object
    path('api/token/', obtain_auth_token, name="obtain-token"),



    # head over to Postman and pass http://127.0.0.1:8000/dj-rest-auth/login (notice how it also includes /login/ as an endpoint) as your url and 
    # select POST and the for the key-value part, you basically do the same things as line 23-24
    # also, for endpoints other than /login/, you might want to check: https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
