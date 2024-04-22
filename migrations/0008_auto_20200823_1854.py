# Generated by Django 3.1 on 2020-08-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0007_auto_20180812_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='max_score',
        ),
        migrations.RemoveField(
            model_name='question',
            name='min_score',
        ),
        migrations.RemoveField(
            model_name='question',
            name='set',
        ),
        migrations.AddField(
            model_name='essay',
            name='accuracy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='essay',
            name='semantic',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='essay',
            name='tense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='essay',
            name='wordcount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]