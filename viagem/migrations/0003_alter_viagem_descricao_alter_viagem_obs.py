# Generated by Django 5.2 on 2025-04-23 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viagem', '0002_viagem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='descricao',
            field=models.TextField(blank=True, db_default='', default='', null=True),
        ),
        migrations.AlterField(
            model_name='viagem',
            name='obs',
            field=models.TextField(blank=True, db_default='', default='', null=True),
        ),
    ]
