from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name="書名")
    price = models.IntegerField(verbose_name="價格")
    pub_date = models.DateField(verbose_name="出版日期")
    
    bread = models.IntegerField(verbose_name="閱讀數") 
    bcomment = models.IntegerField(verbose_name="評論量") 
    
    publish = models.ForeignKey("Publish",on_delete=models.CASCADE,verbose_name="出版社")
    # authors = models.ManyToManyField("Author",verbose_name="作者")

    def __str__(self):
        return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32,verbose_name="出版社名")
    email = models.EmailField(verbose_name="出版社電郵")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name="作者")
    age = models.IntegerField(verbose_name="年齡")

    def __str__(self):
        return self.name
    
    
class Student(models.Model):
    # 模型字段
    name = models.CharField(max_length=100,verbose_name="姓名")
    sex = models.BooleanField(default=1,verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_null = models.CharField(max_length=5,verbose_name="班级编号")
    description = models.TextField(max_length=1000,verbose_name="學生描述")

    class Meta:
        db_table="tb_student"