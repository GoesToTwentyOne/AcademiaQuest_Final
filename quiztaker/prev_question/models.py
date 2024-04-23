from django.db import models

# Create your models here.
class Prev_Questions(models.Model):
    Semester = models.CharField(max_length=40)
    LT = models.CharField(max_length=20,null=False)
    previous_question = models.FileField(upload_to='previous_questions/', null=True, blank=True)
    def __str__(self):
        return f"Semester: {self.Semester}    Level/Term : {self.LT}"
    
    
