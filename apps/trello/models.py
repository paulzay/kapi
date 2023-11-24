from django.db import models

class Timestamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       abstract = True
    
class Column(Timestamps):
    name = models.CharField(max_length=100)
    column_id = models.CharField(max_length=255, primary_key=True)
    def __str__(self):
        return self.name
    
class Task(Timestamps):
    task_id = models.CharField(max_length=255, primary_key=True)
    text = models.CharField(max_length=255)
    column = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.text

