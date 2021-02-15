# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from utils import rpclib
from lib import juicychain


@api_view(['GET'])
def kvupdate1(request, format=None):
    juicychain.connect_node()
    # rpcuser = "changeme"
    # rpcpassword = "alsochangeme"
    # rpcport = 31678
    # rpc_connection = rpclib.rpc_connect(rpcuser, rpcpassword, rpcport)
    # return Response(rpclib.getinfo(rpc_connection), status=status.HTTP_201_CREATED)
    # return Response(juicychain.check_sync(), status=status.HTTP_201_CREATED)
    data = {"this": "is", "a": "json"}
    return Response(juicychain.kvupdate_wrapper("chirs", data, "10", "if mylo agrees"), status=status.HTTP_201_CREATED)
