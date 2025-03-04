# Generated by Django 3.2.5 on 2022-02-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0025_auto_20220130_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='home_page_display',
            field=models.CharField(blank=True, choices=[('Featured', 'Featured'), ('Exclusive', 'Exclusive')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Draft', 'Draft'), ('Published', 'Published'), ('Created', 'Created')], default='Draft', max_length=20),
        ),
    ]
