# Generated by Django 4.2 on 2023-04-14 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_certificado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificado',
            old_name='certicado',
            new_name='certificado',
        ),
    ]
