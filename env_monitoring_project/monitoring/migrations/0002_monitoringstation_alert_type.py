# Generated by Django 5.1.3 on 2024-11-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoringstation',
            name='alert_type',
            field=models.CharField(choices=[('fire', 'Fire'), ('wildlife', 'Wildlife')], default='wildlife', max_length=50),
        ),
    ]