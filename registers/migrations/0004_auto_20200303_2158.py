# Generated by Django 2.2.9 on 2020-03-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0003_auto_20200228_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('CSE', 'CSE'), ('Mechanical', 'Mechanical'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Mechatronics', 'Mechatronics'), ('Chemical', 'Chemical'), ('IT', 'IT')], max_length=254),
        ),
    ]
