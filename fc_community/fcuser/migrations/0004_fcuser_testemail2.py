# Generated by Django 2.1.7 on 2020-08-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_fcuser_testemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcuser',
            name='testEmail2',
            field=models.EmailField(default='tt@tt.com', max_length=128, verbose_name='사용자이메일1'),
        ),
    ]
