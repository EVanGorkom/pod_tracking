# Generated by Django 5.0.2 on 2024-08-04 06:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CardColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.card')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.color')),
            ],
            options={
                'unique_together': {('card', 'color')},
            },
        ),
        migrations.AddField(
            model_name='card',
            name='colors',
            field=models.ManyToManyField(through='v1.CardColor', to='v1.color'),
        ),
    ]