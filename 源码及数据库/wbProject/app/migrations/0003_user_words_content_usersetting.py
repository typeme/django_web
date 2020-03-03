# Generated by Django 2.2.5 on 2019-12-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_books_'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_words_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=45, null=True)),
                ('book_id', models.CharField(blank=True, max_length=45, null=True)),
                ('word', models.TextField(blank=True, null=True)),
                ('part_of_speech', models.TextField(blank=True, null=True)),
                ('chinese', models.TextField(blank=True, null=True)),
                ('sentence', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=45, null=True)),
                ('learn_num', models.IntegerField(blank=True, null=True)),
                ('review_num', models.IntegerField(blank=True, null=True)),
                ('total_words', models.IntegerField(blank=True, null=True)),
                ('learned_num', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
