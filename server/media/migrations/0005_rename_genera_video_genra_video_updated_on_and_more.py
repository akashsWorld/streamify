# Generated by Django 5.0.6 on 2024-06-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_video_upload_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='genera',
            new_name='genra',
        ),
        migrations.AddField(
            model_name='video',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='uploaded_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]