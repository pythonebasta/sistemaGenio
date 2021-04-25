from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from PIL import Image
from PIL.ExifTags import TAGS
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import *
from .models import miaImmagine
import subprocess
import os
import Genio

infoDict = {}
#imgPath = ""
def index_view(request):
  
    return render(request, 'index.html')

#@login_required(login_url='/admin/')
def upload_view(request):
    # miaLista =[]
    # mioDict = {}

    if request.method == 'POST':
        form = ImmaginiForm(request.POST, request.FILES)

        if form.is_valid():
            
            uploadedImage = form.save()
            
            APP_ROOT = os.path.abspath(Genio.__path__[0])

            PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))

            imgPath = PROJECT_PATH + str(uploadedImage.Immagine.url)
            #imgPath = "/home/crislab/Scrivania/sistemaGENIO/sistemaGenio" + str(uploadedImage.Immagine.url)
            #print(imgPath)
            exeProcess = "hachoir-metadata"
            process = subprocess.Popen([exeProcess,imgPath],
                                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                            universal_newlines=True)

            for tag in process.stdout:
                line = tag.strip().split(':')
                infoDict[line[0].strip()] = line[-1].strip()
            for k,v in infoDict.items():
                print(k,':', v)
                #miaLista.append(v)

            try:
                try:
                    if '- Image width' in infoDict:
                        uploadedImage.Image_Width = infoDict.get('- Image width')
                except:
                    uploadedImage.Image_Width = " "
                try:
                    if '- Image height' in infoDict:
                        uploadedImage.Image_Height = infoDict.get('- Image height')
                except:
                    uploadedImage.Image_Height = " "
                try:
                    if '- Bits/pixel' in infoDict:
                        uploadedImage.Bits_Pixel = infoDict.get('- Bits/pixel')
                except:
                    uploadedImage.Bits_Pixel = " "
                try:
                    if '- Pixel format' in infoDict:
                        uploadedImage.Pixel_Format = infoDict.get('- Pixel format')
                except:
                    uploadedImage.Pixel_Format = " "
                try:
                    if '- Compression' in infoDict:
                        uploadedImage.Compression_Rate = infoDict.get('- Compression')  
                except:
                    uploadedImage.Compression_Rate = " "
                try:
                    if '- Image DPI width' in infoDict:
                        uploadedImage.Image_DPI_Width = infoDict.get('- Image DPI width')  
                except:
                    uploadedImage.Image_DPI_Width = " "
                try:
                    if '- Image DPI height' in infoDict:
                        uploadedImage.Image_DPI_Height = infoDict.get('- Image DPI height') 
                except:
                    uploadedImage.Image_DPI_Height = " "   
                try: 
                    if '- Format version' in infoDict:
                        uploadedImage.Compression = infoDict.get('- Format version') 
                except:
                    uploadedImage.Compression = " "
                try:
                    if '- MIME type' in infoDict:
                        uploadedImage.MIME_Type = infoDict.get('- MIME type')                      
                except:
                    uploadedImage.MIME_Type = " "
                try:
                    if '- Endianness' in infoDict:
                        uploadedImage.Endianness = infoDict.get('- Endianness')  
                except:
                    uploadedImage.Endianness = " "

                uploadedImage.save()
            except:
                
                uploadedImage.Image_Width = " "
                uploadedImage.Image_Height = " "
                uploadedImage.Bits_Pixel = " "
                uploadedImage.Pixel_Format = " "
                uploadedImage.Compression_Rate = " "   
                uploadedImage.Image_DPI_Width = " "
                uploadedImage.Image_DPI_Height = " "
                uploadedImage.Compression = " "
                uploadedImage.MIME_Type = " "                      
                uploadedImage.Endianness = " " 

                uploadedImage.save()
            #return HttpResponse(infoDict)
            #return redirect('success', {'imgPath' : imgPath})
            #print(miaLista)
            
            #todo:
            #leggere l'ultimo record inserito e ricavare la pk per indirizzare il response sull'immagine inserita
            ultima = miaImmagine.objects.order_by('id').last()
            #miaId = ultima[id]
            #print(ultima.pk)
            #image_data = open(imgPath, "rb").read()
            #return HttpResponse(image_data, content_type="image/png")
            #return HttpResponse(request.FILES, content_type="image/png")
            #html= "Immagine inserita con successo!  " + '<a href="/images/' + str(ultima.pk) + '>Immagini</a>'
            #return HttpResponse(miaLista)
            return redirect("/images/" + str(ultima.pk))
            #return HttpResponse(html)
    else:
        form = ImmaginiForm()
    return render(request, 'upload.html', {'form' : form})
  
  
# def success(request):
    
#     return HttpResponse('Immagine inserita con successo!')

class ImageListView(ListView):
    model = miaImmagine
    template_name = "display_images.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["im"] = miaImmagine.objects.all()
        return context

class DetailViewCB(DetailView):
    model = miaImmagine
    template_name = "detail_image.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["imd"] = obj = miaImmagine.objects.get(pk=self.object.pk)
        return context



def display_quotazioni(request):
    
    return HttpResponse("FUNZIONALITA' IN PROGETTAZIONE...")

# def display_images(request):
  
#     if request.method == 'GET':
  
#         # getting all the objects of image
#         Immagini = miaImmagine.objects.all() 
#         return render(request, 'display_images.html',
#                      {'images' : Immagini})



