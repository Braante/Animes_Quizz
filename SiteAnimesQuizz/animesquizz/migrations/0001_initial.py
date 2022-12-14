# Generated by Django 4.1.2 on 2022-10-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anime',
            fields=[
                ('idAnime', models.IntegerField(primary_key=True, serialize=False)),
                ('libelleAnime', models.CharField(max_length=50)),
                ('categorie', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'anime',
            },
        ),
        migrations.CreateModel(
            name='anime_genre',
            fields=[
                ('idGenre', models.IntegerField(primary_key=True, serialize=False)),
                ('idAnime', models.IntegerField()),
            ],
            options={
                'db_table': 'anime_genre',
            },
        ),
        migrations.CreateModel(
            name='contenu_question',
            fields=[
                ('idContenu', models.IntegerField(primary_key=True, serialize=False)),
                ('libelleContenu', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'contenu_question',
            },
        ),
        migrations.CreateModel(
            name='genre',
            fields=[
                ('idGenre', models.IntegerField(primary_key=True, serialize=False)),
                ('libelleGenre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('idQuestion', models.IntegerField(primary_key=True, serialize=False)),
                ('libelleQuestion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='reponse',
            fields=[
                ('idQuestion', models.IntegerField(primary_key=True, serialize=False)),
                ('idContenu', models.IntegerField()),
                ('correct', models.BooleanField()),
            ],
            options={
                'db_table': 'reponse',
            },
        ),
    ]
