from django.contrib.auth.models import auth
from django.db import transaction
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# from concession_app.models import *
# from concession_app.helpers import *
# from concession_app.serializers import *
from backend import settings

from pinata import Pinata

pinata = Pinata(settings.PINATA_API_KEY, settings.PINATA_API_SECRET, settings.PINATA_ACCESS_TOKEN)



class UploadToPinataIPFS(APIView):

    permission_classes = []
    authentication_classes = []

    @transaction.atomic
    def post(self, request):

        # input_file = request.FILES["input_file"]
        input_file = f"{settings.BASE_DIR}/static/test_img/img1.png"

        response = pinata.pin_file(input_file)
        print("response :: ", response)
        print("response type :: ", type(response))

        return Response({"success": True, "message": "Successful!"})





