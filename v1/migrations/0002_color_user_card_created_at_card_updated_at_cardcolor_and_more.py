# Generated by Django 5.0.2 on 2024-08-05 01:41

import django.db.models.deletion
import django.utils.timezone
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='CardColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
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
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('tcg', models.CharField(max_length=50)),
                ('deck_type', models.CharField(choices=[('commander', 'COMMANDER'), ('standard', 'STANDARD'), ('modern', 'MODERN'), ('pioneer', 'PIONEER')], max_length=50, null=True)),
                ('colors', models.CharField(blank=True, default='', max_length=100)),
                ('photo', models.URLField(blank=True, null=True)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deck_leader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='v1.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='v1.user')),
            ],
        ),
    ]