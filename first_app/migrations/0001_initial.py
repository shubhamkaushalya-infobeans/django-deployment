# Generated by Django 4.1 on 2023-07-05 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('book_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
                ('email', models.TextField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentBooks',
            fields=[
                ('rel_id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.books')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.student')),
            ],
        ),
    ]
