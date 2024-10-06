from django.db import models
from user.models import User




# Create your models here.
class Category(models.Model):  #یه سلف ریلیشن با خودش داره صرفا
    parent_category = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True) #توضیحات لازم را دادم). که دقیقا چیه ERD اینکه نال و بلنک را ترو میذاریم یعنی اینکه اون فیلد میتونه خالی باشه و ممکنه که اون کتگوری ما پرنتی نداشته باشه و اوکی هم هست بهش می‌گن تاپ‌لول کتگوری. (در ابتدای نوت گوشیم موقع کشیدن
    #the term 'self' refers to the same model class, allowing for a self-referential foreign key.
    title = models.CharField(max_length=200)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    # User: This specifies the model that the foreign key points to (in this case it would be 'User' model that we've definded lately).Each instance of the 'Post' model will be linked to a specific user.
    # on_delete=models.CASCADE: This parameter specifies the behavior to adopt when the referenced user is deleted.
    # CASCADE: If the user associated with a post is deleted, then the corresponding post will also be deleted automatically. This is useful for maintaining data integrity, ensuring that there are no orphaned posts left in the database if their associated user is removed.
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # models.SET_NULL: If the referenced category is deleted, set the category field in the post to NULL. This requires that the field is nullable (null=True).
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, related_name="liked_posts", null=True, blank=True) #در یک فیلدش آیدی پست و در دیگری آیدی یوزر است و مااز تیبل میانی که به واسطه این ریلیشن منی تو منی ایجاد شده متوجه می‌شیم که هر یوزری چه پستی را لایک کرده و یا مثلا تعداد لایک‌های یک پستی چندتا بوده LikeUserPost اسمش رو گذاشتیم ERD وقتی بین دو تا مدل ریلیشن منی تو منی برقراره، توی یکی‌شون هم بنویسم این ریلیشن رو کافیه . و معمولا در مدلی که بعدا ساخته میشه اون ریلیشن رو می‌نویسن. الان مثلا لازم نیست توی مدل یوزر هم برم و این خط رو بنویسم و این فیلد منی تو منی میاد بین اون دو تا تیبل (مدل) یدونه تیبل میانی درست می‌کنه که همونطور که در .
    # In your Django model, the 'related_name' attribute in the 'ManyToManyField' for the 'liked_by' field specifies the name of the reverse relation from the 'User' model back to your 'Post' model.



class Comment(models.Model):  #اگر قابلیت ریپلای زدن به یک کامنت را هم بخواهیم فعال کنیم، باید به خودش فارن کی بزنیم و همون سلف ریلیشن خودمون میشه
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()