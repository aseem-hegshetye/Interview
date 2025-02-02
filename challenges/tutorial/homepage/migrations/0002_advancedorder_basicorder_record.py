# Generated by Django 2.2.2 on 2019-06-10 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='advancedOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='basicOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('cellphone', models.CharField(default=None, max_length=10, null=True)),
                ('workphone', models.CharField(default=None, max_length=10, null=True)),
                ('email', models.EmailField(default=None, max_length=254, null=True)),
                ('address', models.CharField(default=None, max_length=100, null=True)),
                ('protectionPlan', models.BooleanField(default=None, null=True)),
                ('advancedOrder', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.advancedOrder')),
                ('basicOrder', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.basicOrder')),
            ],
        ),
    ]
