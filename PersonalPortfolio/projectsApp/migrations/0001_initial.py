# Generated by Django 5.1.2 on 2024-11-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('image', models.ImageField(default='images/default.jpg', upload_to='projects/')),
                ('type', models.CharField(choices=[('Web Application', 'Web Application'), ('Mobile Application', 'Mobile Application'), ('Infrastructure As A Service', 'Iaas'), ('Cloud', 'Cloud'), ('Server Less Application', 'Serverless')], max_length=120)),
                ('status', models.BooleanField(default=True)),
                ('link', models.CharField(max_length=1024)),
            ],
        ),
    ]
