# Generated by Django 5.2 on 2025-04-16 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='apps.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chinese_character', models.CharField(max_length=10)),
                ('pinyin', models.CharField(max_length=50)),
                ('english_translation', models.CharField(max_length=255)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='apps.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option_a', models.CharField(max_length=255)),
                ('option_b', models.CharField(max_length=255)),
                ('option_c', models.CharField(max_length=255)),
                ('option_d', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='apps.lesson')),
            ],
        ),
    ]
