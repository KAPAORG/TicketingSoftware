# Generated by Django 3.2.5 on 2021-07-24 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='Status',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='summary',
            field=models.CharField(max_length=200),
        ),
    ]
