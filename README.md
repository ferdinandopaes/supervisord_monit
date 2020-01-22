# Supervisord Monit

Supervisord Monit is a python script that help to discovery, create itens and triggers on Zabbix.

#### Minimum requirements

- Zabbix v4.0
- Python2.7

#### Setup

- On file named `/etc/supervisor/supervisord.conf` add lines:
```
[inet_http_server]
port = 127.0.0.1:9001

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface
```

- Reload supervisord service;

- Add file named `userparameter_supervisor.conf` into `/etc/zabbix/zabbix_agentd.d`;

- Add files named `supervisor.py` and `queues.py` into `/etc/zabbix/scripts`;

- Restart Zabbix Agent;
