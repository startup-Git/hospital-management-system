# Generated by Django 4.0.4 on 2022-11-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0003_patientsreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientsreview',
            name='Email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patientsreview',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
