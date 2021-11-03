# Generated by Django 3.2.2 on 2021-11-02 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('last_name', models.CharField(blank=True, max_length=80, verbose_name='last name')),
                ('phone_number', models.BigIntegerField(verbose_name='phone number')),
                ('address', models.CharField(blank=True, max_length=180)),
            ],
        ),
    ]