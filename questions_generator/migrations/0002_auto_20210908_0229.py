# Generated by Django 3.0.7 on 2021-09-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions_generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='quiz_type',
        ),
        migrations.RenameField(
            model_name='quizes',
            old_name='topic',
            new_name='organization',
        ),
        migrations.AlterField(
            model_name='quizes',
            name='exam_title',
            field=models.CharField(default='New_Quiz_89202122922', max_length=200),
        ),
    ]
