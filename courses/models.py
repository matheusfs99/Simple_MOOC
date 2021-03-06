from django.db import models
from django.urls import reverse

# Create your models here.
class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) |
                                          models.Q(description__icontains=query))


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    slug = models.SlugField(verbose_name='Atalho')
    description = models.TextField(verbose_name='Descrição', blank=True)
    about = models.TextField(verbose_name='Sobre o Curso', blank=True)
    start_date = models.DateField(verbose_name='Data de Início', null=True, blank=True)
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:details', args=(self.slug,))

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['name']