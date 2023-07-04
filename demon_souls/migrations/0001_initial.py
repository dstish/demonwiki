# Generated by Django 4.2.1 on 2023-07-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='items/images/')),
                ('category', models.CharField(choices=[('weapon', 'Weapon'), ('armor', 'Armor'), ('ring', 'Ring'), ('magic', 'Magic'), ('character', 'Character'), ('boss', 'Boss'), ('location', 'Location')], default='weapon', max_length=100)),
            ],
        ),
    ]
