# Generated by Django 3.2.7 on 2021-09-23 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cislo', models.IntegerField()),
                ('Film', models.TextField(max_length=255)),
                ('Actor', models.TextField(max_length=255)),
                ('Country', models.TextField(max_length=255)),
                ('Rez', models.TextField(max_length=255)),
            ],
        ),
    ]
