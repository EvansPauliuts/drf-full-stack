from rest_framework import serializers

from core.abstract import AbstractSerializer
from core.comment.models import Comment
from core.post.models import Post
from core.user.models import User
from core.user.serializers import UserSerializer


class CommentSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='public_id')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        return rep

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'author',
            'body',
            'edited',
            'created',
            'updated',
        )
        read_only_fields = ('edited',)

    def validate_post(self, value):
        return self.instance.post if self.instance else value

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True

        instance = super().update(instance, validated_data)
        return instance
