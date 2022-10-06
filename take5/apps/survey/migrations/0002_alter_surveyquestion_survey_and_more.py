# Generated by Django 4.1.2 on 2022-10-06 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="surveyquestion",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="survey.survey",
            ),
        ),
        migrations.AlterField(
            model_name="surveyquestionalternative",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="alternatives",
                to="survey.surveyquestion",
            ),
        ),
    ]
