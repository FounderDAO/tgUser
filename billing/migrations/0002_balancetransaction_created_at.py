# Generated by Django 3.0.2 on 2021-07-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='balancetransaction',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]