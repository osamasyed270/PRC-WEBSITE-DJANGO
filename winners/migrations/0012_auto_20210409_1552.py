# Generated by Django 3.1.7 on 2021-04-09 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('winners', '0011_auto_20210409_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winner',
            name='categories',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='winners.category'),
        ),
    ]
