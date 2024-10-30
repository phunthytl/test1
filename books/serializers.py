from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("__all__")

class GetAllBookSerializer(serializers.ModelSerializer):
    the_loai = serializers.CharField(source='the_loai.name', read_only=True)
    class Meta:
        model = Book
        fields = ("__all__")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)
