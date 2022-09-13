from rest_framework import serializers

from .models import Post


# being familiar with forms and defining them, serializers would come easy to understand
# what serializers do is they convert out models into JSON
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner',
        )