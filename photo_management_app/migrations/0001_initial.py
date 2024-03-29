# Generated by Django 4.2.9 on 2024-01-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='images')),
                ('uploader', models.CharField(default='sahar', max_length=255)),
                ('caption', models.CharField(max_length=255, verbose_name='légende')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
