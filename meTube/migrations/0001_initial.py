# Generated by Django 3.2.2 on 2021-06-07 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='First Name')),
                ('surname', models.CharField(max_length=256, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('avatar', models.ImageField(height_field=500, upload_to='avatar/', verbose_name='Avatar', width_field=500)),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now_add=True, verbose_name='Date Updated')),
            ],
            options={
                'verbose_name': 'AppUser',
                'verbose_name_plural': 'AppUsers',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256, verbose_name='Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meTube.appuser', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tile')),
                ('caption', models.CharField(max_length=256, verbose_name='Caption')),
                ('date_added', models.DateTimeField(auto_now=True, verbose_name='Date Added')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meTube.appuser', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meTube.comment', verbose_name='Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meTube.appuser', verbose_name='User')),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meTube.appuser', verbose_name='User')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meTube.video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meTube.video', verbose_name='Video'),
        ),
    ]
