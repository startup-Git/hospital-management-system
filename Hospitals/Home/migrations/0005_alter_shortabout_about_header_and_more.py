# Generated by Django 4.0.4 on 2022-10-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_shortabout_about_header_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortabout',
            name='about_header',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shortabout',
            name='about_image_one',
            field=models.ImageField(blank=True, null=True, upload_to='Home-page'),
        ),
        migrations.AlterField(
            model_name='shortabout',
            name='about_image_three',
            field=models.ImageField(blank=True, null=True, upload_to='Home-page'),
        ),
        migrations.AlterField(
            model_name='shortabout',
            name='about_image_two',
            field=models.ImageField(blank=True, null=True, upload_to='Home-page'),
        ),
        migrations.AlterField(
            model_name='shortabout',
            name='about_services_header',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shortabout',
            name='about_services_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shortabout',
            name='header_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shortabout',
            name='image_two_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
