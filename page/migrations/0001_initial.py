# Generated by Django 3.0.7 on 2020-06-29 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=200)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('value_type', models.CharField(max_length=200)),
            ],
        ),
    ]
