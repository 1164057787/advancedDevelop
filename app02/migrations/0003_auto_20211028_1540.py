# Generated by Django 2.2 on 2021-10-28 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0002_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='adminid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
