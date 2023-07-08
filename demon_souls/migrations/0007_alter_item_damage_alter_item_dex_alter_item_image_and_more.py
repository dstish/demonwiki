# Generated by Django 4.2.1 on 2023-07-07 22:20

import demon_souls.item_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demon_souls', '0006_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='damage',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='dex',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=demon_souls.item_models.get_image_upload_path),
        ),
        migrations.AlterField(
            model_name='item',
            name='str',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]