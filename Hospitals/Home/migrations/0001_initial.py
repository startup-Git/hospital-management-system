# Generated by Django 4.0.4 on 2022-10-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='Slider')),
                ('Time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]