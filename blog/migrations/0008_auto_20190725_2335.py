# Generated by Django 2.2.3 on 2019-07-25 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blog_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='come',
            new_name='comment',
        ),
    ]