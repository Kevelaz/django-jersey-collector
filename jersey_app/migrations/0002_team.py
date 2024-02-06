# Generated by Django 5.0.1 on 2024-02-06 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jersey_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colorway', models.CharField(max_length=30)),
                ('years_on_team', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('jersey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jersey_app.jersey')),
            ],
        ),
    ]