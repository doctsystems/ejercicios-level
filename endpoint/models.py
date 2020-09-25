from django.db import models
from django.core.exceptions import ValidationError

class Persona(models.Model):
	nombre=models.CharField(max_length=50)
	email=models.EmailField(unique=True)
	kms=models.IntegerField(default=0)

	def clean(self):
		if self.kms<4:
			raise ValidationError('Debes de caminar mas...', code='kms')

	def save(self):
		self.nombre=self.nombre.upper()
		super(Persona, self).save()

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural='Personas'
