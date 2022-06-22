# Generated by Django 4.0.5 on 2022-06-19 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companies',
            fields=[
                ('uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('name', models.CharField(max_length=300, null=True)),
                ('discription', models.CharField(max_length=300, null=True)),
                ('url', models.CharField(max_length=300, null=True)),
                ('url_company', models.CharField(max_length=300, null=True)),
                ('data_small_loaded', models.DateField(null=True)),
                ('data_full_loaded', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='people',
            fields=[
                ('uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('second_name', models.CharField(max_length=150, null=True)),
                ('full_name', models.CharField(max_length=300, null=True)),
                ('url', models.CharField(max_length=300, null=True)),
                ('discription', models.CharField(max_length=300, null=True)),
                ('location', models.CharField(max_length=300, null=True)),
                ('data_small_loaded', models.DateField(null=True)),
                ('data_full_loaded', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='people_experience',
            fields=[
                ('uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('job_discription', models.CharField(max_length=300, null=True)),
                ('job_timing_type', models.CharField(max_length=50, null=True)),
                ('data_small_loaded', models.DateField(null=True)),
                ('companies', models.ForeignKey(db_column='uuid_companies', on_delete=django.db.models.deletion.CASCADE, to='com_linkedin.companies')),
                ('people', models.ForeignKey(db_column='uuid_people', on_delete=django.db.models.deletion.CASCADE, to='com_linkedin.people')),
            ],
        ),
    ]