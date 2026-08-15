from rest_framework import serializers
from prueba_tecnica.models import Author

class PopularAuthorsSerializer(serializers.ModelSerializer):

    top_authors = serializers.IntegerField(read_only=True)

    class Meta:
        
        model = Author
        fields = ['id','name','top_authors']
        read_only_fields = ['id']
        