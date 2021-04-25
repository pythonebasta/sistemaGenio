from django import forms
from .models import *
  
class ImmaginiForm(forms.ModelForm):
  
    class Meta:
        model = miaImmagine
        fields = ['Nome', 'Immagine','Image_Width','Image_Height','Bits_Pixel','Pixel_Format','Compression_Rate',
        'Image_DPI_Width','Image_DPI_Height','Compression','MIME_Type','Endianness']
                
         
        widgets = {'Image_Width': forms.HiddenInput(),'Image_Height': forms.HiddenInput(),'Bits_Pixel': forms.HiddenInput(),
             'Pixel_Format': forms.HiddenInput(),  'Compression_Rate': forms.HiddenInput(),'Image_DPI_Width': forms.HiddenInput(),
             'Image_DPI_Height': forms.HiddenInput(),'Compression': forms.HiddenInput(),'MIME_Type': forms.HiddenInput(),
             'Bits_Pixel': forms.HiddenInput(),'Endianness': forms.HiddenInput()
        
        }

    
      
