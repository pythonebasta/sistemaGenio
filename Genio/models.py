from django.db import models
from django.urls import reverse

# Create your models here.

class miaImmagine(models.Model):
    Nome = models.CharField(max_length=50)
    Immagine = models.ImageField(upload_to='images/')
    Image_Width = models.CharField(max_length=50, blank=True)
    Image_Height = models.CharField(max_length=50, blank=True)
    Bits_Pixel = models.CharField(max_length=50, blank=True)
    Pixel_Format = models.CharField(max_length=50, blank=True)
    Compression_Rate = models.CharField(max_length=50, blank=True)
    Image_DPI_Width = models.CharField(max_length=50, blank=True)
    Image_DPI_Height = models.CharField(max_length=50, blank=True)
    Compression = models.CharField(max_length=50, blank=True)
    MIME_Type = models.CharField(max_length=50, blank=True)
    Endianness = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.Nome

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})