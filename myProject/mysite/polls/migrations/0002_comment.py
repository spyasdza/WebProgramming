# Generated by Django 2.1.7 on 2019-04-24 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
    ]
