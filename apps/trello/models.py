from django.db import models

class Column(models.Model):
    name = models.CharField(max_length=100)
    column_id = models.CharField(max_length=255, primary_key=True)
    def __str__(self):
        return self.name
    
class Task(models.Model):
    task_id = models.CharField(max_length=255, primary_key=True)
    text = models.CharField(max_length=255)
    column = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return self.text