# Generated by Django 5.1.2 on 2024-11-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('Photo Session', 'Photo Session'), ('Programming Project', 'Programming Project'), ('Consultant', 'Consultant')], max_length=50)),
                ('quantity', models.SmallIntegerField(default=1)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Preset Filter', 'Preset Filter'), ('Photo Session', 'Photo Session'), ('Programming Project', 'Programming Project'), ('Consultant', 'Consultant')], max_length=50),
        ),
    ]
