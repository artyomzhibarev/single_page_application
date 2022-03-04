from django.db import models


class Entity(models.Model):
    create_at = models.DateTimeField(auto_created=True, verbose_name='Created at')
    name = models.CharField(max_length=255, verbose_name='Name')
    count = models.IntegerField(verbose_name='Count')
    distance = models.IntegerField(verbose_name='Distance')

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'

    def __str__(self):
        return self.name
