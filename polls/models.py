import datetime
from django.contrib import admin

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    # id는 직접 입력 안해도 자동으로 생성됨
    question_text = models.CharField(max_length=200) #질문내용, 문자(Char), 최대길이 200자
    pub_date = models.DateTimeField('date published') #발행 날짜, 날짜시간
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #선택지에 대한 질문, 외래키? Question이라는 데이터 모델을 참조하겠다는 뜻, cascade-->질문이 삭제되면 답변도 삭제됨
    #Django 는 다-대-일(many-to-one), 다-대-다(many-to-many), 일-대-일(one-to-one) 과 같은 모든 일반 데이터베이스의 관계들를 지원
    choice_text = models.CharField(max_length=200) #선택내용
    votes = models.IntegerField(default=0) #투표수, 정수(Integer)
    
    def __str__(self):
        return self.choice_text
    
    
    # python3 manage.py makemigrations polls
    # makemigrations 을 실행시킴으로서, 당신이 모델을 변경시킨 사실과(이 경우에는 새로운 모델을 만들었습니다) 이 변경사항을 migration으로 저장시키고 싶다는 것을 Django에게 알려줍니다.
    # 데이터베이스 내의 테이블을 생성하기 위한 설계도가 만들어짐
    
    # python3 manage.py migrate
    # migrate 를 실행시켜 데이터베이스에 모델과 관련된 테이블을 생성