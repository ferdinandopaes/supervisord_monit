# Monitoramento do Supervisord

Template criado para monitorar o serviço do supervisord e também os status das filas criadas por ele no laravel

#### Requisitos mínimos

- Testado com Zabbix v4.0
- Python2.7

#### Configuração

- No arquivo `/etc/supervisor/supervisord.conf` adicione as seguintes linhas:
```
[inet_http_server]
port = 127.0.0.1:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
```

- Execute o reload do serviço do supervisord;

- Adicione o arquivo `userparameter_supervisor.conf` no diretório `/etc/zabbix/zabbix_agentd.d`;

- Adicione os arquivos `supervisor.py` e `queues.py` no diretório `/etc/zabbix/scripts`;

- Reinicie o serviço do agente Zabbix;
