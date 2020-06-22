# Generated by Django 3.0 on 2020-06-13 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='playerInfo',
            new_name='playersInfo',
        ),
        migrations.AddField(
            model_name='tournament',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]