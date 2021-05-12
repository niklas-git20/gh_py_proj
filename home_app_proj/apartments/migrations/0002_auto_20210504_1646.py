# Generated by Django 3.1.3 on 2021-05-04 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apart',
            options={'ordering': ['nbr']},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'ordering': ['last_name']},
        ),
        migrations.AlterField(
            model_name='apart',
            name='layout',
            field=models.ImageField(upload_to='apart'),
        ),
        migrations.AlterField(
            model_name='apart',
            name='summary',
            field=models.TextField(help_text='Enter a appartment info', max_length=1000),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_req', models.CharField(blank=True, choices=[('e', 'electric'), ('s', 'sanitary')], default='s', help_text='Required service type', max_length=1)),
                ('req_date', models.DateField(blank=True, null=True)),
                ('avail_date', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
