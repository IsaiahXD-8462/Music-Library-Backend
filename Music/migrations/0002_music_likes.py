# Generated by Django 4.2 on 2023-04-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]