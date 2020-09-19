# Generated by Django 3.1.1 on 2020-09-19 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200918_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='saccum_volume',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='accum_volume',
            field=models.CharField(default='default_title', max_length=255, verbose_name='Объем батареи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=True, verbose_name='Наличие SD карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_max',
            field=models.CharField(max_length=255, null=True, verbose_name='Максимальный обьем встроенной памяти'),
        ),
    ]
