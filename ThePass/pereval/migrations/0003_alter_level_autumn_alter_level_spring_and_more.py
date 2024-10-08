# Generated by Django 5.0.6 on 2024-05-28 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0002_alter_level_autumn_alter_level_spring_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(choices=[('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('1Б', '1Б'), ('3Б', '3Б'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Осень'),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(choices=[('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('1Б', '1Б'), ('3Б', '3Б'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Весна'),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(choices=[('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('1Б', '1Б'), ('3Б', '3Б'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Лето'),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(choices=[('2А', '2А'), ('2Б', '2Б'), ('3А', '3А'), ('1Б', '1Б'), ('3Б', '3Б'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Зима'),
        ),
        migrations.AlterField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('accepted', 'Принят'), ('new', 'Новый'), ('pending', 'В работе'), ('rejected', 'Отклонён')], default='new', max_length=8),
        ),
    ]
