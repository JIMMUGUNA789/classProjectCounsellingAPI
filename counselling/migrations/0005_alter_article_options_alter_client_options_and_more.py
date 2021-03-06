# Generated by Django 4.0.5 on 2022-06-22 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0004_issue'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_published'], 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='counsellor',
            options={'verbose_name_plural': 'Counsellors'},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'verbose_name_plural': 'Issues'},
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('expired', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling.client')),
                ('counsellor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='counselling.counsellor')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
