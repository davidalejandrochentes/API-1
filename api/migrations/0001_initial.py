# Generated by Django 4.2.6 on 2023-10-08 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]