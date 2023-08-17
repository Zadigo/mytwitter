# Generated by Django 3.2.8 on 2021-11-30 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='visibility',
            field=models.CharField(choices=[('Public', 'Public'), ('Followers', 'Followers'), ('Mentionned', 'Mentionned')], default='Public', max_length=100),
        ),
        migrations.AddField(
            model_name='reply',
            name='visibility',
            field=models.CharField(choices=[('Public', 'Public'), ('Followers', 'Followers'), ('Mentionned', 'Mentionned')], default='Public', max_length=100),
        ),
    ]