# Generated by Django 2.2.9 on 2020-02-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_cell', '0005_auto_20200209_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image_logo',
            field=models.FileField(blank=True, upload_to='post-image'),
        ),
    ]