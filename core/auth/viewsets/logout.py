from rest_framework import permissions, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class LogoutViewSet(viewsets.ViewSet):
    authentication_classes = ()
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')

        if refresh is None:
            raise ValidationError({'detail': 'A refresh token is required.'})

        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TokenError as e:
            raise ValidationError({'detail': 'The refresh token is invalid.'}) from e
