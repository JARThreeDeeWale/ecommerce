# Generated by Django 3.1.2 on 2020-10-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='reference',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
