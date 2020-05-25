# Generated by Django 3.0 on 2020-05-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='discord_handle',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tco_handle',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True, verbose_name='TCO handle'),
        ),
    ]
