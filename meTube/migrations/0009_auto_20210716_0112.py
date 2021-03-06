# Generated by Django 3.2.2 on 2021-07-16 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meTube', '0008_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='meTube.appuser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_video', to='meTube.video', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to='meTube.appuser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='like',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_video', to='meTube.video', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='meTube.comment', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_user', to='meTube.appuser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='meTube.appuser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='view',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewer', to='meTube.appuser', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='view',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_video', to='meTube.video', verbose_name='Video'),
        ),
    ]
