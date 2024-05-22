# Generated by Django 4.0.4 on 2022-10-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_shortdoctortitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortDoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_profile', models.ImageField(blank=True, null=True, upload_to='Home-page')),
                ('doctor_name', models.CharField(blank=True, max_length=120, null=True)),
                ('specialist', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_icon_class', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook_profile', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin_icon_class', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin_profile', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp_icon_class', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp_profile', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]