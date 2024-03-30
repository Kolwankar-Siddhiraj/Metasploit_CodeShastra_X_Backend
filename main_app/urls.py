from django.urls import path
from main_app.views import *


urlpatterns = [
    path('upload-to-ipfs', UploadToPinataIPFS.as_view(), name="upload-to-ipfs")
]

