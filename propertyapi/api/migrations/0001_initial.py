# Generated by Django 5.1.4 on 2024-12-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('house', 'House'), ('villas', 'Villas'), ('flat', 'Flat')], max_length=10)),
                ('bedroom_count', models.IntegerField()),
                ('square_footage', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
