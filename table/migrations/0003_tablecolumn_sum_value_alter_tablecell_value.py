# Generated by Django 5.0.7 on 2024-07-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_alter_tablecell_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablecolumn',
            name='sum_value',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tablecell',
            name='value',
            field=models.FloatField(null=True),
        ),
    ]
