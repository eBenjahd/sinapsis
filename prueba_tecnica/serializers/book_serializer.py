from rest_framework import serializers
from prueba_tecnica.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ['id','title','author','isbn','published_date','copies_available']
        read_only_fields = ['id','copies_available']