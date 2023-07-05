from django.conf import settings

from core.abstract import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AUTO_FIELD
            return representation

        if settings.DEBUG:
            request = self.context.get('request')
            representation['avatar'] = request.build_absolute_uri(representation['avatar'])

            return representation

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'is_active',
            'created',
            'updated',
        )
        read_only_field = ('is_active',)
