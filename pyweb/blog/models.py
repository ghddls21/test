from django.db import models

# Create your models here.

class BlogTable(models.Model):
    제목 = models.CharField(max_length=200, blank=False, null=False)
    내용 = models.TextField(blank=True, null=True)
    조회수 = models.IntegerField(null=False)
    작성자 = models.CharField(max_length=50, null=False)
    등록일 = models.DateTimeField(null=False)
    수정일 = models.DateTimeField(null=False)

    def __str__(self):
        return str(self.id) + ', ' + self.제목