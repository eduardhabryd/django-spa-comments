from django.db import models


class Comment(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField()
    home_page = models.URLField(blank=True)
    text = models.TextField()
    parent_comment = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name="replies"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.created_at}'
