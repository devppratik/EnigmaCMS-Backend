# Generated by Django 3.2.5 on 2022-02-05 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0039_auto_20220205_1223'),
    ]

    operations = [
        # migrations.RenameField(
        #     model_name='article',
        #     old_name='tag',
        #     new_name='tags',
        # ),
        # migrations.RemoveField(
        #     model_name='tag',
        #     name='articles',
        # ),
        migrations.AlterField(
            model_name='article',
            name='home_page_display',
            field=models.CharField(blank=True, choices=[('Exclusive', 'Exclusive'), ('Featured', 'Featured')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Published', 'Published'), ('Draft', 'Draft'), ('Created', 'Created')], default='Draft', max_length=20),
        ),
    ]
