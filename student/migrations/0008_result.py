# Generated by Django 2.2 on 2019-10-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20191005_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('gpa', models.IntegerField()),
            ],
        ),
    ]
