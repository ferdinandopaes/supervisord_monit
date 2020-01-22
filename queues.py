##
# Script gera a lista de filas do supervisor para criar itens no zabbix
# Criado por: Ferdinando Paes
# Criado em 2020-01-14
##

import xmlrpclib, sys

def get_data(argument):
    server = xmlrpclib.Server('http://localhost:9001/RPC2')
    #print(argument)
    process = server.supervisor.getProcessInfo(argument)
    print (process['state'])

arg = sys.argv[1]
get_data(arg)
