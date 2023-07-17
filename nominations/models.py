from django.db import models

# Create your models here.

class Voter(models.Model):
    studentid = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=12, null=False)
    address = models.CharField(max_length=30)
    student_email = models.EmailField()
    student_password = models.CharField(max_length=100, null=True)

class Position(models.Model):
    position = models.CharField(max_length=50, primary_key=True)
    description = models.TextField()
    
class Nomination(models.Model):
    nomineeID = models.IntegerField(primary_key=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    session = models.IntegerField(default=0)
    year = models.IntegerField(null=True)
    n_desc = models.TextField()

class Vote(models.Model):
    nomineeID = models.ForeignKey(Nomination, on_delete=models.CASCADE, related_name='nominee_votes')
    studentid = models.ForeignKey(Voter, on_delete=models.CASCADE, related_name='student_votes')
    votedate = models.DateTimeField()