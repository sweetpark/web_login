# Generated by Django 4.1.1 on 2022-10-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=20)),
                ('userpw', models.CharField(max_length=20)),
            ],
        ),
    ]
