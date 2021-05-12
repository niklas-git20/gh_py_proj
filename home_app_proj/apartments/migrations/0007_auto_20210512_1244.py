# Generated by Django 3.1.3 on 2021-05-12 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apartments', '0006_auto_20210512_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accrual',
            name='accrued',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accrual',
            name='balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accrual',
            name='confirm',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='accrual',
            name='contrib',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='accrual',
            name='nbr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]