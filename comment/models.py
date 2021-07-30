from django.db import models
from django.conf import settings
from issue.models import Issues

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=500, blank=True)
    author_comment = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_comment')
    issue = models.ForeignKey(to=Issues, on_delete=models.CASCADE, related_name="comment", null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.comment_id) + ' ' + str(self.description)
