# Generated by Django 3.1.7 on 2021-05-04 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='content',
        ),
    ]
