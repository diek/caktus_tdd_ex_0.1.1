# Generated by Django 3.2.12 on 2022-04-11 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('byline', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clue_text', models.CharField(max_length=512)),
                ('theme', models.BooleanField(default=False)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='xword_data.entry')),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='xword_data.puzzle')),
            ],
        ),
    ]
