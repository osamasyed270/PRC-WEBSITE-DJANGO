# Generated by Django 3.1.7 on 2021-03-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_match_1_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match_1_register',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
