
from django.urls import path
from book.apis import BookAPIView

urlpatterns = [
    path('', BookAPIView.as_view(), name='books-api'),
]