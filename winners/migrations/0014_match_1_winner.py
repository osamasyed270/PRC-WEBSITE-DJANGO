# Generated by Django 3.1.7 on 2021-04-12 17:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('winners', '0013_auto_20210412_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match_1_Winner',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('image_url', models.CharField(blank=True, max_length=1000)),
                ('full_name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='male', max_length=100)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
