# Generated by Django 3.2 on 2021-04-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genio', '0003_miaimmagine_image_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='miaimmagine',
            name='Bits_Pixel',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='Compression',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='Compression_Rate',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='Endianness',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='Image_DPI_Height',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='Image_DPI_Width',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='Image_Height',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='MIME_Type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='miaimmagine',
            name='Pixel_Format',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='miaimmagine',
            name='Image_Width',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
