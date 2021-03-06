# Generated by Django 3.1.7 on 2021-03-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=20)),
                ('info1', models.CharField(max_length=20)),
                ('number', models.PositiveIntegerField(verbose_name=3)),
            ],
        ),
        migrations.CreateModel(
            name='LandRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=20)),
                ('info1', models.CharField(max_length=20)),
                ('number', models.PositiveIntegerField(verbose_name=3)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.CharField(max_length=20)),
                ('parcel', models.CharField(max_length=20)),
                ('number', models.PositiveIntegerField(verbose_name=3)),
            ],
        ),
    ]
