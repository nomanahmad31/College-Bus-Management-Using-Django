# Generated by Django 2.1.1 on 2020-06-09 08:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buses', '0003_auto_20200608_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_generation_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.Bus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]