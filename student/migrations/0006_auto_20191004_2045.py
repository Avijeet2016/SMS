# Generated by Django 2.2 on 2019-10-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='roll',
        ),
        migrations.AddField(
            model_name='studentdetailinfo',
            name='roll',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
