from django.db import models

# Create your models here.

class Tables(models.Model):
	caf_name = models.CharField(max_length=50)
	tablenum = models.PositiveIntegerField()

	def __str__(self):
		return self.caf_name

class Occupancy(models.Model):
	table=models.CharField(max_length=50)
	customer_email=models.EmailField()

	def __str__(self):
		return self.customer_email