# Generated by Django 3.0 on 2020-05-30 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20200530_0220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deckregistration',
            old_name='photo_verification_link',
            new_name='verification_photo_url',
        ),
    ]