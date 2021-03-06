# Generated by Django 3.2.4 on 2021-06-30 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210630_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='additional_service',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='files_boleta',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='files_causa',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='type_service',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
