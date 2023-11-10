from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class TodoList(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lists")
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self) -> str:
        return f"{self.title}"

class TodoItem(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="items")
    
    def __str__(self) -> str:
        return f"{self.todo_list}-{self.title}"
    
    class Meta():
        ordering = ["-created"]
