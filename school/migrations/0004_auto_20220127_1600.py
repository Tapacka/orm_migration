# Generated by Django 3.1.2 on 2022-01-27 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20220127_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='students', to='school.Teacher'),
        ),
    ]
