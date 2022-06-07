# Generated by Django 4.0.5 on 2022-06-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='counsellor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
