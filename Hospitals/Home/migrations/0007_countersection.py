# Generated by Django 4.0.4 on 2022-10-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_shortdepartment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CounterSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_video', models.FileField(blank=True, null=True, upload_to='videos')),
                ('counter_icon', models.CharField(blank=True, max_length=100, null=True)),
                ('counter_icon_title', models.CharField(blank=True, max_length=200, null=True)),
                ('counter_value', models.IntegerField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]