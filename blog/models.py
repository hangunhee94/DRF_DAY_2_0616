from django.db import models
from datetime import timezone
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField("이름",max_length=30)
    description = models.TextField("설명")

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    user = models.ForeignKey('user.User',verbose_name="작성자",on_delete=models.CASCADE, max_length=30)
    category = models.ManyToManyField(Category,verbose_name="카테고리", null=True)
    # category = models.ForeignKey(Category,verbose_name="카테고리",on_delete=models.CASCADE)
    title = models.CharField("제목",max_length=30)
    contents = models.TextField("내용")
    exposure_start_date = models.DateField("노출 시작 일자", default=timezone.now)
    exposure_end_date = models.DateField("노출 종료 일자", default=timezone.now)


    def __str__(self):
        return f'{self.title} {self.user.username}님이 작성하신 글입니다.'

class Comment(models.Model):
    article = models.ForeignKey('blog.Article',verbose_name="게시글",on_delete=models.CASCADE, max_length=30)
    user = models.ForeignKey('user.User',verbose_name="작성자",on_delete=models.CASCADE, max_length=30)
    contents = models.TextField("내용", max_length=300)

    def __str__(self):
        return f'{self.contents} {self.user.username}님이 작성하신 댓글입니다.'
