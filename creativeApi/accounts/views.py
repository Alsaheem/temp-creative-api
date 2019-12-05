from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from accounts.models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework import filters
############################### User Follow section ###############################
# To be able to follow or unfollow a user

class UserFollowAPIView(APIView):
    '''
    follow users and can unfollow users
    '''
    serializer_class = UserProfileSerializer

    def delete(self, request, username):
        who_to_unfollow = User.objects.get(username=username)  #i hope the slug is the user to be followed thoo 
        user = UserProfile.objects.get(user=request.user)  #this is the user that wants to follow someone
        user.followers.remove(who_to_unfollow)

    def post(self, request, username):
        who_to_follow = User.objects.get(username=username)  #i hope the slug is the user to be followed thoo 
        user = UserProfile.objects.get(user=request.user)  #this is the user that wants to follow someone
        user.followers.add(who_to_follow)

class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username','email',)

