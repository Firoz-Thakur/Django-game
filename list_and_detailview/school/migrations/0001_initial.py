# Generated by Django 3.1.5 on 2021-03-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=43)),
                ('roll', models.IntegerField()),
                ('course', models.CharField(max_length=43)),
            ],
        ),
    ]