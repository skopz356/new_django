# Generated by Django 2.0.6 on 2018-06-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=300)),
                ('prize', models.FloatField(max_length=20)),
            ],
        ),
    ]
