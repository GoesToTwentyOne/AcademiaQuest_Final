# Generated by Django 4.2.4 on 2023-09-03 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_quizrating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='has_time_limit',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
