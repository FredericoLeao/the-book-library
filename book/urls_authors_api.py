
from django.urls import path
from book.apis import AuthorAPIView

urlpatterns = [
    path('', AuthorAPIView.as_view(), name='books-api'),
]