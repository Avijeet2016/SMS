# Generated by Django 2.2 on 2019-10-04 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20191004_2045'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student', 'date')},
        ),
        migrations.AlterUniqueTogether(
            name='studentdetailinfo',
            unique_together={('roll', 'std_class')},
        ),
    ]