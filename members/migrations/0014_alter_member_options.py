# Generated by Django 3.2.5 on 2021-11-07 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_alter_member_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['first_name']},
        ),
    ]
