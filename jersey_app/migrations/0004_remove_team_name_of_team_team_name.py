# Generated by Django 5.0.1 on 2024-02-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jersey_app', '0003_team_name_of_team_alter_team_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='name_of_team',
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]