# Generated by Django 3.0.2 on 2020-03-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard1', '0004_auto_20200318_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedback_que',
            field=models.CharField(default='', max_length=3000),
        ),
    ]
