# Generated by Django 5.0.4 on 2024-04-12 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='X',
            field=models.CharField(default='', max_length=50),
        ),
    ]
