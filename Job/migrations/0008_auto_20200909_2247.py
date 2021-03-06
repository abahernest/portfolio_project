# Generated by Django 3.1.1 on 2020-09-09 21:47

from django.db import migrations
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0007_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(blank=True, upload_to='image/'),
        ),
    ]
