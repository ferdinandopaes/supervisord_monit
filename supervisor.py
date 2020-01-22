##
# Script gera a lista de filas do supervisor para criar itens no zabbix
# Criado por: Ferdinando Paes
# Criado em 2020-01-14
##

import xmlrpclib, json

def list_queues():
    server = xmlrpclib.Server('http://localhost:9001/RPC2')

    allProcess = server.supervisor.getAllProcessInfo()
    lista = []

    for i in allProcess:
        lista.append({"{#GROUP}": i["group"], "{#NAME}": i["name"]})

    dic = {}
    dic['data'] = lista
    dataJson = json.dumps(dic)
    print (dataJson)

list_queues()
