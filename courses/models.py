from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    slug = models.SlugField(verbose_name='Atalho')
    description = models.TextField(verbose_name='Descrição', blank=True)
    start_date = models.DateField(verbose_name='Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem')
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)