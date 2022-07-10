# Generated by Django 4.0.5 on 2022-06-10 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='brand_type',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='discrete_video_card',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='graphic_card_type',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='guaranty',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='has_hdd',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='has_ssd',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='memory_type',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='ram_memory_type',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='screen_diagonal_type',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='brand_type',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='change',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='dual_sim',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='face_id',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='guaranty',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='memory_type',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='network',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='nfc',
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='ram_memory_type',
        ),
        migrations.AddField(
            model_name='laptop',
            name='brand',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='smartphone',
            name='brand',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='laptopimage',
            name='images',
            field=models.ImageField(default=1, upload_to='electronic/laptop_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='smartphoneimage',
            name='images',
            field=models.ImageField(default=1, upload_to='electronic/smartphone_images/'),
            preserve_default=False,
        ),
    ]