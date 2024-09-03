# Generated by Django 5.1.1 on 2024-09-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_at', 'title')},
        ),
        migrations.AlterField(
            model_name='article',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='uploads/PostsImages'),
        ),
    ]
