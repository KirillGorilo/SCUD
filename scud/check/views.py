from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from users.models import User
import qrcode
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.http import JsonResponse



def home(request):
    return render(request, 'check/home.html')


def generate_qr_code(request):
    user = User.objects.get(id=request.user.id)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    url = "http://192.168.252.200/find_user" + user.identity_qrcode
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    response = HttpResponse(content_type="image/png")

    img.save(response, "PNG")
    return response


def update_id_now(request):
    user = User.objects.get(id=request.user.id)
    user.update_id()
    return HttpResponseRedirect(reverse('home'))


@login_required
def find_user(request, user_id):
    try:
        print(id)
        user = User.objects.get(identity_qrcode=user_id)
        return render(request, 'check/user_profile.html', {'user': user})
    except User.DoesNotExist:
        return render(request, 'check/not_exists.html', {'error_message': "Пользователь не найден!!!"})


# REST API
class GenerateQRCodeView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        id = user_id

        if not id:
            return JsonResponse({'error': 'ID пользователя не указан'}, status=400)

        try:
            user = User.objects.get(id=id)
            user.update_id()
            url = "http://192.168.252.200:8000/find_user/" + user.identity_qrcode
            return JsonResponse({'url': url}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'error': 'Пользователь с таким ID не найден!!!'}, status=404)