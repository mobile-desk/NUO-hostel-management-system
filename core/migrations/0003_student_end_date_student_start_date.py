# Generated by Django 4.2.1 on 2023-09-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_student_address_of_guardian_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='end_date',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='start_date',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
