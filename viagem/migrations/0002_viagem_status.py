# Generated by Django 5.2 on 2025-04-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viagem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='viagem',
            name='status',
            field=models.IntegerField(db_default=1),
        ),
    ]
