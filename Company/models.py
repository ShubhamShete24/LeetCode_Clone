from django.db import models
from ProblemCreation.models import ProblemCreation


# Create your models here.
class CompanyName(models.Model):
    companyName = models.CharField(max_length=100, unique=True)


class CompanyProblem(models.Model):
    companyID = models.ForeignKey(CompanyName, on_delete=models.PROTECT)
    problemID = models.ForeignKey(ProblemCreation, on_delete=models.PROTECT)
