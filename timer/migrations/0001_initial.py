# Generated by Django 2.0.6 on 2018-06-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_title', models.CharField(max_length=50)),
                ('activity_time', models.IntegerField(default=0)),
            ],
        ),
    ]
