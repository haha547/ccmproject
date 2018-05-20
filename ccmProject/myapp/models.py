from django.db import models

class Employee (models.Model):
	name = models.CharField(max_length = 50)
	position = models.CharField(max_length = 50)
	account = models.CharField(max_length = 50)
	password = models.CharField(max_length = 50)
	def __str__ (self):
		return self.name
"""
^c
python manage.py makemigrations更新資料庫
python manage.py migrate 同步資料庫即可
python manage.py runserver
"""