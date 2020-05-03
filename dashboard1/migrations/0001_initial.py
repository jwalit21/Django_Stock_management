# Generated by Django 3.0.2 on 2020-02-29 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=100)),
                ('stock_id', models.CharField(max_length=20)),
                ('stock_prize', models.IntegerField()),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
    ]
