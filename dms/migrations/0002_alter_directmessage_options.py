# Generated by Django 3.2.8 on 2021-11-30 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='directmessage',
            options={'ordering': ['created_on', 'pk']},
        ),
    ]
