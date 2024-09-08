from django.db import models

class Task(models.Model):
 title=models.CharField(max_length=255)
 description=models.TextField(blank=True,null=True)
 priority= models.IntegerField(default=1,choices=[(1,'High'),(2,'Medium'),(3,'Low')])
 status=models.CharField(default='To Do',choices=[('To Do','To Do'), ('In Progress','In Progress'), ('Done','Done')],max_length=255)
 due_date=models.DateField( blank=True)

 def __str__(self):
  return self.title
