# Generated by Django 2.2.6 on 2019-10-11 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='user',
        ),
    ]