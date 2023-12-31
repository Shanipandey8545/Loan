# Generated by Django 4.1.1 on 2023-04-02 11:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0003_homeloan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personalloan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.IntegerField(max_length=50)),
                ('employeetype', models.IntegerField(max_length=100000)),
                ('apply_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
