# Generated by Django 2.2.5 on 2021-04-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Default Value', max_length=256),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='Default Value', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='Default Value', max_length=14),
        ),
        migrations.AddField(
            model_name='user',
            name='post_code',
            field=models.CharField(default='Default Value', max_length=250),
        ),
    ]
