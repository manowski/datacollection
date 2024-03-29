# Generated by Django 3.2.3 on 2021-08-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiktokUserDailyStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('followers_count', models.IntegerField(default=0)),
                ('following_count', models.IntegerField(default=0)),
                ('likes_count', models.BigIntegerField(default=0)),
                ('likes_given_count', models.IntegerField(default=0)),
                ('video_count', models.IntegerField(default=0)),
                ('user_avg_likes', models.BigIntegerField(default=0)),
                ('user_avg_plays', models.BigIntegerField(default=0)),
                ('user_avg_comments', models.BigIntegerField(default=0)),
                ('user_avg_shares', models.BigIntegerField(default=0)),
                ('engagement_rate', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.tiktokuser')),
            ],
        ),
    ]
