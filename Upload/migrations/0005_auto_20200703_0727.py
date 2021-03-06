# Generated by Django 2.1.5 on 2020-07-03 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Upload', '0004_remove_uploads_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Upload.Uploads'),
        ),
        migrations.AlterField(
            model_name='postimages',
            name='post_imgs',
            field=models.FileField(default='default.png', upload_to='post_photo/'),
        ),
    ]
