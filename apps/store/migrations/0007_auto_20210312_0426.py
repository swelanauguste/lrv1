# Generated by Django 3.1.7 on 2021-03-12 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20210312_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='number',
            field=models.CharField(max_length=3, null=True),
        ),
    ]