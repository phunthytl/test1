from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .serializers import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ListBookByCategoryView(APIView):  
     def get(self, request, category_name):
        try:
            category = Category.objects.get(name=category_name)  # Lấy category theo tên
            books = Book.objects.filter(the_loai=category)  # Lọc sách theo thể loại
            mydata = BookViewSet(books, many=True)
            return Response(mydata.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
class GetAllCategory(APIView):
    def get(self, request):
        categories = Category.objects.all()
        mydata = CategorySerializer(categories, many=True)
        return Response(mydata.data, status=status.HTTP_200_OK)

# class GetAllBookAPIView(APIView):
#     def get(self, request):
#         list_book = Book.objects.all()
#         mydata = GetAllBookSerializer(list_book, many=True)
#         return Response(mydata.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         mydata = GetAllBookSerializer(data=request.data)
#         if mydata.is_valid():
#             mydata.save()   
#             return Response(mydata.data, status=status.HTTP_201_CREATED)
#         return Response(mydata.data, status=status.HTTP_400_BAD_REQUEST)
    
# class BookInfo(APIView):
#     def get(self, request, id):
#         try:
#             a_book = Book.objects.get(id_book = id)
#         except Book.DoesNotExist():
#             msg = {"msg":"not found"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         mydata = GetAllBookSerializer(a_book)
#         return Response(mydata.data, status=status.HTTP_200_OK)
    
#     def put(self, request, id):
#         try:
#             a_book = Book.objects.get(id_book = id)
#         except Book.DoesNotExist():
#             msg = {"msg":"not found error"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         mydata = GetAllBookSerializer(a_book, data = request.data)
#         if mydata.is_valid():
#             mydata.save()
#             return Response(mydata.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(mydata.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, id):
#         try:
#             a_book = Book.objects.get(id_book = id)
#         except Book.DoesNotExist():
#             msg = {"msg":"not found error"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         mydata = GetAllBookSerializer(a_book, data = request.data, partial=True)
#         if mydata.is_valid():
#             mydata.save()
#             return Response(mydata.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(mydata.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id):
#         try:
#             a_book = Book.objects.get(id_book = id)
#         except Book.DoesNotExist():
#             msg = {"msg":"not found error"}
#             return Response(msg, status=status.HTTP_404_NOT_FOUND)
#         a_book.delete()
#         return Response({"msg":"deleted"}, status=status.HTTP_204_NO_CONTENT)



