# Generated by Django 4.0.3 on 2022-03-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('distance', models.IntegerField()),
            ],
        ),
    ]
