# Generated by Django 3.2.8 on 2021-11-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
