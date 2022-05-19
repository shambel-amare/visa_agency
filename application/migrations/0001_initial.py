# Generated by Django 4.0.4 on 2022-05-19 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=20, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('application_type', models.PositiveSmallIntegerField(choices=[(1, 'Business'), (2, 'Work'), (3, 'School'), (4, 'Medical')], default=2)),
                ('phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('Address', models.CharField(blank=True, max_length=20, null=True)),
                ('passport_number', models.CharField(blank=True, max_length=20, null=True)),
                ('passport_photo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
