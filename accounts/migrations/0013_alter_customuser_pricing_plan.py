# Generated by Django 4.0.5 on 2022-07-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_customuser_pricing_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pricing_plan',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
