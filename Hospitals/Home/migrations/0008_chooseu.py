# Generated by Django 4.0.4 on 2022-10-28 10:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_countersection'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_us_image', models.ImageField(blank=True, null=True, upload_to='Home-page')),
                ('choose_us_description', models.CharField(blank=True, max_length=200, null=True)),
                ('collapsible_header_icon', models.CharField(blank=True, max_length=100, null=True)),
                ('collapsible_header', models.CharField(blank=True, max_length=255, null=True)),
                ('collapsible_paragraph', tinymce.models.HTMLField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
