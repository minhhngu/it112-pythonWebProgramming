# Generated by Django 3.1.5 on 2021-01-08 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingtitle', models.CharField(max_length=255)),
                ('meetingdate', models.DateField()),
                ('meetingtime', models.TimeField()),
                ('meetinglocation', models.CharField(max_length=255)),
                ('meetingagenda', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resroucename', models.CharField(max_length=255)),
                ('resourcetype', models.CharField(max_length=255)),
                ('resourceurl', models.URLField(blank=True, null=True)),
                ('resourcedate', models.DateField()),
                ('resourcedescription', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'resources',
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='Minute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutestext', models.TextField()),
                ('attendence', models.ManyToManyField(related_name='attendence', to=settings.AUTH_USER_MODEL)),
                ('meetingid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='club.meeting')),
            ],
            options={
                'verbose_name_plural': 'minutes',
                'db_table': 'minute',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(max_length=255)),
                ('eventlocation', models.CharField(max_length=255)),
                ('eventdate', models.DateField()),
                ('eventtime', models.TimeField()),
                ('eventdescription', models.TextField()),
                ('eventuser', models.ManyToManyField(related_name='eventuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
    ]
