# Generated by Django 2.2.1 on 2019-06-12 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0008_auto_20190612_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='hgender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别'),
        ),
    ]
