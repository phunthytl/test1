from django.db import models

# Category
class Category(models.Model):
    id_category = models.AutoField(primary_key=True)  # Khóa chính tự động tăng
    name = models.CharField(max_length=200, null=True, unique=True)  # Tên loại sách

    def __str__(self):
        return self.name

# Book
class Book(models.Model):
    id_book = models.AutoField(primary_key=True)  # Khóa chính tự động tăng
    the_loai = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')  # Liên kết với loại sách
    tieu_de = models.CharField(max_length=200, null=True)  # Tiêu đề sách
    tac_gia = models.CharField(max_length=200, null=True)  # Tác giả
    mo_ta = models.TextField(blank=True)  # Mô tả sách
    noi_dung = models.TextField(null=True)  # Nội dung sách
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Ảnh bìa

    def __str__(self):
        return f"{self.tieu_de}" 