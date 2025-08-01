from django.db import models

class BookAuthors(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    author_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'book_authors'

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    published_year = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'
    
    def __str__(self):
        return self.title


class Author(models.Model):
    # DB의 `id` 필드와 매핑. Unmanaged 모델에서는 primary_key를 명시해주는 것이 좋습니다.
    id = models.AutoField(primary_key=True)

    # DB의 `name` 필드와 매핑 (NOT NULL)
    name = models.CharField(max_length=100)

    # DB의 `country` 필드와 매핑 (NULL 허용)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False  # Django가 이 테이블을 관리하지 않도록 설정
        db_table = 'authors'  # 실제 데이터베이스 테이블 이름 지정

    def __str__(self):
        return self.name