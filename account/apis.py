from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from thebooklibrary.permissions import IsSuperuser
from account.models import User
from account.serializers import UserSerializer

class AccountAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsSuperuser]
    serializer_class = UserSerializer