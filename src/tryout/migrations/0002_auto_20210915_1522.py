# Generated by Django 2.1.5 on 2021-09-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000),
        ),
    ]