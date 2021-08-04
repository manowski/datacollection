from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from src.accounts.models import Account
from src.accounts.permissions import IsUserOrReadOnly
from src.accounts.serializers import CreateAccountSerializer, AccountSerializer


class AccountViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Creates, Updates and Retrieves - User Accounts
    """
    queryset = Account.objects.all()
    serializers = {
        'default': AccountSerializer,
        'create': CreateAccountSerializer
    }
    permissions = {
        'default': (IsUserOrReadOnly,),
        'create': (AllowAny,)
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        self.permission_classes = self.permissions.get(self.action, self.permissions['default'])
        return super().get_permissions()

    @action(detail=False, methods=['get'], url_path='me', url_name='me')
    def get_user_data(self, instance):
        try:
            data = AccountSerializer(self.request.user, context={'request': self.request}).data
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Wrong auth token' + e}, status=status.HTTP_400_BAD_REQUEST)
