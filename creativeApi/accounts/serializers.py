from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import UserProfile

#################### user following serializer ####################

class UserProfileSerializer(serializers.ModelSerializer):
    '''
    a user following serializer that gets the followers snd following
    count, will also check if the user is already followed
    '''
    following_count = serializers.SerializerMethodField(read_only=True)
    followers_count = serializers.SerializerMethodField(read_only=True)
    followers_list = serializers.SerializerMethodField(read_only=True)
    # user_is_following = serializers.SerializerMethodField(read_only=True)
    # followed_on = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"

    def get_following_count(self, instance):
        return instance.following.count()

    def get_followers_count(self, instance):
        return instance.followers.count() 

    def get_followers_list(self, instance):
        return instance.followers.all() 

    # def get_user_is_following(self, instance):
    #     request = self.context.get("request")
    #     return instance.following.filter(slug=request.user.slug).exists()

