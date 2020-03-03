# Generated by Django 3.0.2 on 2020-03-03 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0008_auto_20200303_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.Task'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Task Creation Accepted'), (2, 'Task Creation Rejected'), (3, 'Task Submission Accepted'), (4, 'Task Submission Rejected')], default=1, verbose_name='Vote Type'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
