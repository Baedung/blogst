from django.db import models

# 클래스로서 어떤 종류의 데이터를 처리하고 싶은지 적어준다!
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    # models.~~CharField는 굉장히 많다
    # 이런 작업을 해주는 이유는 장고와 데이터베이스가 별개의 것이기 때문!
    def __str__(self):
        return self.title 
        
    def summary(self):
        return self.body[:100]
        # 100글자를 상한선으로 리턴하라!
        