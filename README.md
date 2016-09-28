# zabbix-mesos-template
Zabbix monitoring template for Mesos 1.0.1 and Zabbix 3.0

### Zabbix server
1. Put getMesosStats.py in your external scripts directory
2. Make it executable (chmod +x ...)

### Zabbix frontend
4. Import templates for master and agent
5. Link it with desired hosts
6. Set {$MESOS_PORT} macro (5050 for masters, 5051 for agents)
