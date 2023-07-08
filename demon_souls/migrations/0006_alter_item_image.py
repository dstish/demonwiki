# Generated by Django 4.2.1 on 2023-07-07 21:49

import demon_souls.item_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demon_souls', '0005_item_attack_type_item_damage_item_dex_item_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='items/images/product-placeholder.jpg', upload_to=demon_souls.item_models.get_image_upload_path),
        ),
    ]