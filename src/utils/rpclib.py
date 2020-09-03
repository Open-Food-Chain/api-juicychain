from slickrpc import Proxy

# class KomododAPI(object):
#  def __init__(self, rpcuser, rpcpassword, rpcport):
#    self.komodod_api = rpc_connect(rpcuser,rpcpassword,rpcport)


def rpc_connect(rpc_user, rpc_password, port):
    try:
        rpc_connection = Proxy("http://%s:%s@127.0.0.1:%d" % (rpc_user, rpc_password, port))
    except Exception:
        raise Exception("Connection error! Probably no daemon on selected port.")
    return rpc_connection


def getinfo(rpc_connection):
    try:
        getinfo = rpc_connection.getinfo()
    except Exception:
        raise Exception("Connection error!")
    return getinfo
