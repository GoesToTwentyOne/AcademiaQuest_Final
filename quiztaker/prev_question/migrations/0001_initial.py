# Generated by Django 5.0.2 on 2024-03-31 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prev_Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Semester', models.CharField(max_length=40)),
                ('LT', models.CharField(max_length=20)),
                ('previous_question', models.ImageField(blank=True, null=True, upload_to='previous_questions/')),
            ],
        ),
    ]