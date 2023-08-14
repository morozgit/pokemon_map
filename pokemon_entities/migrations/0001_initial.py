# Generated by Django 4.2 on 2023-08-14 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('title_jp', models.CharField(max_length=200)),
                ('describe', models.TextField(max_length=1000)),
                ('photo', models.ImageField(null=True, upload_to='pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('appeared_at', models.DateTimeField()),
                ('disappeared_at', models.DateTimeField()),
                ('level', models.IntegerField(default=0)),
                ('heath', models.IntegerField(default=100)),
                ('strength', models.IntegerField(default=0)),
                ('defense', models.IntegerField(default=0)),
                ('stamina', models.IntegerField(default=0)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon')),
            ],
        ),
    ]
