# Generated by Django 5.0.2 on 2024-02-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mana_cost', models.CharField(max_length=50)),
                ('cmc', models.IntegerField(default=0)),
                ('type_line', models.CharField(max_length=255)),
                ('rarity', models.CharField(max_length=50)),
                ('cmdr_legal', models.CharField(max_length=50)),
                ('img', models.URLField()),
                ('purchase_uris', models.URLField()),
            ],
        ),
    ]
