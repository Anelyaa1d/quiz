from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default='')
    like_count = models.IntegerField(read_only=True)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey()

    def to_json(self):
        return{
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at,
            "like_count": self.like_count,
            "created_by": self.created_by
        }

