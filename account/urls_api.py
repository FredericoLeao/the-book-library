
from django.urls import path
from account.apis import AccountAPIView

urlpatterns = [
    path('', AccountAPIView.as_view(), name='accounts-api'),
]