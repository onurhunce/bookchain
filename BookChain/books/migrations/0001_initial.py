# Generated by Django 2.1.3 on 2018-12-13 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=500)),
                ('categories', models.TextField(max_length=500)),
                ('author', models.TextField(max_length=200)),
                ('language', models.TextField(max_length=30)),
                ('genre', models.TextField(max_length=200)),
                ('year', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('languages', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField(max_length=20)),
                ('relation_status', models.TextField(max_length=20)),
                ('action_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_user_1', to=settings.AUTH_USER_MODEL)),
                ('user_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_user_2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Swaps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('book_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_book_1', to='books.Library')),
                ('book_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_book_2', to='books.Library')),
                ('last_action_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_action_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SwapStatuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='swaps',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.SwapStatuses'),
        ),
        migrations.AddField(
            model_name='swaps',
            name='user_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_user_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='swaps',
            name='user_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='swap_user_2', to=settings.AUTH_USER_MODEL),
        ),
    ]
