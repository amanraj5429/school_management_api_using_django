# Generated by Django 4.2.6 on 2023-10-21 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='emergency_contact',
            field=models.CharField(default='TBU', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile_number',
            field=models.CharField(default='TBU', max_length=15),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_guardian',
            field=models.CharField(default='TBU', max_length=10),
        ),
    ]
