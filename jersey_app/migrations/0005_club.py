# Generated by Django 5.0.1 on 2024-02-06 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jersey_app', '0004_remove_team_name_of_team_team_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('year_founded', models.IntegerField()),
                ('country_of_origin', models.CharField()),
                ('league_name', models.CharField()),
            ],
        ),
    ]
