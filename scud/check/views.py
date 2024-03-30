from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
import qrcode
import io


def index(request):
    return render(request, 'check/qrcode.html')
    

class GenerateQRCode(View):
    def get(self, request, *args): 
        data = 'https://google.com'
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")


        response = HttpResponse(content_type='image/png')
        img.save(response, 'PNG')

        return response






