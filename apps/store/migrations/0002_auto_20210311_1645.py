# Generated by Django 3.1.7 on 2021-03-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='status',
            field=models.CharField(choices=[('payment pending', 'payment pending'), ('paid', 'paid'), ('searching', 'searching'), ('printed', 'printed'), ('stamped', 'stamped'), ('delivered', 'delivered')], default='payment pending', max_length=25),
        ),
        migrations.AddField(
            model_name='landregister',
            name='status',
            field=models.CharField(choices=[('payment pending', 'payment pending'), ('paid', 'paid'), ('searching', 'searching'), ('printed', 'printed'), ('stamped', 'stamped'), ('delivered', 'delivered')], default='payment pending', max_length=25),
        ),
        migrations.AddField(
            model_name='search',
            name='status',
            field=models.CharField(choices=[('payment pending', 'payment pending'), ('paid', 'paid'), ('searching', 'searching'), ('printed', 'printed'), ('stamped', 'stamped'), ('delivered', 'delivered')], default='payment pending', max_length=25),
        ),
    ]