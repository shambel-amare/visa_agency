# Generated by Django 4.0.4 on 2022-05-19 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
