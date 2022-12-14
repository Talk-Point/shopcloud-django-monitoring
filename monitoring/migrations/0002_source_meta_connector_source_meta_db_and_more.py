# Generated by Django 4.1.3 on 2022-11-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='meta_connector',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='meta_db',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='type',
            field=models.CharField(choices=[('SQL_QUERY_V1', 'SQL_QUERY_V1'), ('NOT_SUCCESS_V1', 'NOT_SUCCESS_V1'), ('SQL_SAGE_GATEWAY_V1', 'SQL_SAGE_GATEWAY_V1')], max_length=255),
        ),
    ]
