from django.urls import path
from book.apis import CategoryAPIView

urlpatterns = [
    path('', CategoryAPIView.as_view(), name='books-api'),
]
