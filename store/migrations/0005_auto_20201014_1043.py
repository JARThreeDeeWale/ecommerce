# Generated by Django 3.1.1 on 2020-10-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20201013_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]