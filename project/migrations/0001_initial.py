# Generated by Django 4.0.2 on 2022-03-07 06:20

from django.db import migrations, models
import django.db.models.deletion
import project.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('client_name', models.CharField(blank=True, max_length=255, null=True)),
                ('client_services', models.CharField(blank=True, max_length=511, null=True)),
                ('client_website', models.URLField(blank=True, null=True)),
                ('client_phone_number', models.CharField(blank=True, max_length=11, null=True)),
                ('objective', models.TextField(blank=True, null=True)),
                ('challenges', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='project.category')),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=project.models.upload_news_image_path)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_image', to='project.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.ManyToManyField(to='project.Tools'),
        ),
    ]
