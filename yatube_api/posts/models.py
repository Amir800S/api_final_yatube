from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import CheckConstraint, UniqueConstraint

User = get_user_model()


class Group(models.Model):
    """Модель групп."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель Постов."""
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации поста', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель Комментов."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата создания комментария', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Модель подписок."""
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
        null=True
    )
    following = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = 'Лента'
        UniqueConstraint(fields=['author', 'user'],
                         name='re-subscription')
        CheckConstraint(
            name='prevent_self_follow',
            check=~models.Q(user=models.F('author')), )

    def __str__(self):
        return '{} подписан на {}'.format(self.user, self.following)
