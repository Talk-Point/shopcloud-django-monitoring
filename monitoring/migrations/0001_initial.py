# Generated by Django 4.1.3 on 2022-11-19 10:46

from django.db import migrations, models
import django.db.models.deletion
import shopcloud_django_toolbox.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('type', models.CharField(choices=[('SQL_QUERY_V1', 'SQL_QUERY_V1'), ('SAGE_SQL_CONNECTOR_V1', 'SAGE_SQL_CONNECTOR_V1'), ('NOT_SUCCESS_V1', 'NOT_SUCCESS_V1')], max_length=255)),
                ('meta_api_endpoint', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_api_username', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_api_password', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            bases=(shopcloud_django_toolbox.models.GID, models.Model),
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('last_run_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_ok', models.BooleanField(default=True)),
                ('query', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('value', models.IntegerField(blank=True, null=True)),
                ('value_min', models.IntegerField(blank=True, null=True)),
                ('value_max', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metrics', to='monitoring.source')),
            ],
            bases=(shopcloud_django_toolbox.models.GID, models.Model),
        ),
    ]
