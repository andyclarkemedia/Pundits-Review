# Generated by Django 3.0.7 on 2020-06-26 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_club_clubscore_clubsentence'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubscore',
            name='club',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='club_scores', to='main.Club'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clubsentence',
            name='club',
            field=models.ForeignKey(default=22, on_delete=django.db.models.deletion.CASCADE, related_name='club_sentences', to='main.Club'),
            preserve_default=False,
        ),
    ]