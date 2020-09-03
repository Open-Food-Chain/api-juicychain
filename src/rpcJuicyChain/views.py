# from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import rpclib


@api_view(['GET'])
def getinfo(request, format=None):
    rpcuser = "user1750295076"
    rpcpassword = "pass4d3581fbc864bf66cd00fee33fb40eee0fa0b0f1ae07ecf17a4ad581db752ad249"
    rpcport = 8096
    rpc_connection = rpclib.rpc_connect(rpcuser, rpcpassword, rpcport)
    return Response(rpclib.getinfo(rpc_connection), status=status.HTTP_201_CREATED)
