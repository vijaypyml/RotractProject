# Generated by Django 3.0.8 on 2020-07-21 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs',
            name='ClubID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='ClubName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='District_Mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Group',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Group_Mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Password',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='President_Mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='President_Name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Secretary_Mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Secretary_Name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Sponsoring',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Sponsoring_Mail',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clubs',
            name='Username',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('ProjectId', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectType', models.CharField(max_length=200, null=True)),
                ('ProjectDate', models.DateTimeField(null=True)),
                ('PrjectTime', models.TimeField(null=True)),
                ('EventChair', models.CharField(max_length=200, null=True)),
                ('Speaker', models.CharField(max_length=200, null=True)),
                ('Description', models.CharField(max_length=200, null=True)),
                ('PoterPic', models.ImageField(blank=True, null=True, upload_to='')),
                ('Username', models.ForeignKey(max_length=32, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
