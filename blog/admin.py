from django.contrib import admin
from .models import Post, Comment, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "parent_category"]
    search_fields = ["title"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "category", "posted_on"]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment_abbreviation", "user", "post"]  #نوشتم و حالا پایینش اگه بیایید یک متد دقیقا به همون اسم بنویسید توی ریترنش اونو نمایش می‌ده "comment_abbreviation" اینجا توی این لیست ما یک اسم دلخواه می‌تونیم بنویسیم من
    search_fields = ["text", "user", "post"]

    def comment_abbreviation(self, cm):
        return cm         # همان کامنت است که اینستنسی از کلاس کامنت است حالا ما وقتی این اینتستنس رو ریترن می‌کنیم یعنی داریم پرینتش می‌کنیم حالا وقتی پرینتش می‌کنیم چه متدی فراخوانی میشه؟ همون متد اس‌تی‌آر که در فایل مدل‌ها برای مدل کامنت نوشتیم و حالا وقتی اون فراخوانی میشه با توجه به متد اس‌تی‌آر ایی که در کلاس کامنت در فایل مادلز نوشتم میره تکستش رو درمیاره و تا 7 تا کاراکتر اولش رو می‌نویسه cm منظور از
