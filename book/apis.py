from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from book.models import (
    Book,
    Author,
    Category
)
from book.serializers import (
    BookSerializer,
    AuthorSerializer,
    CategorySerializer
)


class BookAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class AuthorAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

