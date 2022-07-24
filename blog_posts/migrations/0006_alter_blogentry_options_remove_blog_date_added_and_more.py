# Generated by Django 4.0.6 on 2022-07-24 03:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0005_rename_blog_blog_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogentry',
            options={'verbose_name_plural': 'Blog Entries'},
        ),
        migrations.RemoveField(
            model_name='blog',
            name='date_added',
        ),
        migrations.AddField(
            model_name='blogentry',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
