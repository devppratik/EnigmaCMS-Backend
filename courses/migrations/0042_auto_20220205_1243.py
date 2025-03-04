# Generated by Django 3.2.5 on 2022-02-05 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0041_auto_20220205_1241'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='article',
        #     name='tags',
        #     field=models.ManyToManyField(blank=True, to='courses.Tag'),
        # ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('Published', 'Published'), ('Rejected', 'Rejected'), ('Created', 'Created'), ('Draft', 'Draft')], default='Draft', max_length=20),
        ),
    ]
