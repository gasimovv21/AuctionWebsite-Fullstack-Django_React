from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils import getPaypalDataDetail


@api_view(['GET'])
def getPaypalData(request):
    if request.method == 'GET':
        return getPaypalDataDetail(request)
