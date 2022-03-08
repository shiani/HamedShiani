# Generated by Django 4.0.2 on 2022-03-08 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HireMeSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HireMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=38)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire_me.hiremesubject')),
            ],
        ),
    ]
