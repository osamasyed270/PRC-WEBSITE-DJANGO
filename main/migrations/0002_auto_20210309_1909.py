# Generated by Django 3.1.7 on 2021-03-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match1',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='match1',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
