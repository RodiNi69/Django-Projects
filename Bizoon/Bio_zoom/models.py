from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Sum


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    e_mail = models.EmailField(max_length=150, null=True)
    rank = models.IntegerField(default=0)
    id_users = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def update_rating(self):
        a = Post.objects.filter(id_author=self.id).aggregate(Sum('sum_rank'))['sum_rank__sum'] * 3
        b = Comments.objects.filter(id_users=self.id_users).aggregate(Sum('sum_rank'))['sum_rank__sum']
        c = Post.objects.filter(id_author=self.id).values('id')
        d = 0
        for i in c:
            com = Comments.objects.filter(id_post=i['id']).aggregate(Sum('sum_rank'))['sum_rank__sum']
            if com:
                d += com
        self.rank = a + b + d
        self.save()


POSITIONS = [('news', 'Новости'), ('article', 'Статьи')]


class SubscribersUsers(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, through=SubscribersUsers)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    head_article = models.CharField(max_length=255)
    text_post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    type_post = models.CharField(max_length=20, choices=POSITIONS, default='news')
    sum_rank = models.IntegerField(default=0)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.sum_rank = self.sum_rank+1
        self.save()

    def dislike(self):
        if self.sum_rank > 0:
            self.sum_rank = self.sum_rank-1
            self.save()

    def preview(self):
        return self.text_post[0:124]

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])


class PostCategory(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comments(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sum_rank = models.IntegerField(default=0)
    id_users = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.sum_rank = self.sum_rank+1
        self.save()

    def dislike(self):
        if self.sum_rank > 0:
            self.sum_rank = self.sum_rank-1
            self.save()

    def preview(self):
        return self.text_post[0:124]

    def get_absolute_url(self):
        return reverse('news', args = [str(self.id)])

