# Monitoring (telegraf, influxdb, grafana) 

Это наиболее низкоуровневая, наиболее оптимальная по производительности и гибкости система.

## Telegraf агент
Может быть установлен на другой сервер и пересылать метрики, а также логи в базы influxdb, elasticsearch, prometheus или graphite, а также в несколько серверов очередей. Единственный его недостаток: он умеет парсить только один файл. Поэтому, если нужно проверять несколько журналов, придется использовать несколько процессов.

## Influxdb
База данных, которая может принимать данные из telegraf, netdata или collectd. построенная для обработки высоких нагрузок на запись и запрос. InfluxDB — это специализированное высокопроизводительное хранилище данных, написанное специально для временных данных (мониторинг DevOps, метрики приложений, данные датчика IoT и аналитика в реальном времени). Оно позволяет сохранять пространство на своем компьютере, настраивая InfluxDB для хранения данных в течение определенного периода времени и по его истечению — автоматического удаления любых нежелательных данных из системы.

 ## Grafana 
 Grafana позволяет визуализировать данные из influxdb, elasticsearch, clickhouse, prometheus, graphite, а также отправлять уведомления на почту, в slack и telegram.

## How to install
Prerequisite:
- ubuntu 18.04
- ip 10.200.12.190
- adminki / Password12!

### 1. influxdb 
    # curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
    # echo "deb https://repos.influxdata.com/debian stretch stable" > /etc/apt/sources.list.d/influxdata.list
    # apt-get update
    # apt-get install influxdb
    # systemctl start influxdb

в итоге, теперь можно делать запросы к базе (правда данных там ещё пока нет):
http://localhost:8086/query?q=select+*+from+telegraf..cpu:

    root@monitoring-tig:~# influx
    Connected to http://localhost:8086 version 1.7.1
    InfluxDB shell version: 1.7.1
    Enter an InfluxQL query

Create the database:

    > CREATE DATABASE telegraf
    > SHOW DATABASES
    name: databases
    name
    ----
    _internal
    telegraf

Create a user:

    > CREATE USER telegraf WITH PASSWORD 'Password12!'
    > GRANT ALL ON telegraf TO telegraf
    > SHOW USERS;
    user     admin
    ----     -----
    telegraf false

### 2. telegraf
    apt install telegraf
    systemctl start telegraf

Configure Telegraf (backup the configuration file):

    cp /etc/telegraf/telegraf.conf /etc/telegraf/telegraf.conf.orig

Agent configuration:

    [agent]
        flush_interval = "15s"
        interval = "15s"
        hostname = "monitoring-tig"

Basic inputs configuration, e.g. probes:

    [[inputs.cpu]]
    [[inputs.mem]]
    [[inputs.system]]
    [[inputs.disk]]
        mount_points = ["/"]
    [[inputs.processes]]
    [[inputs.net]]
        fieldpass = [ "bytes_*" ]

To see all the inputs available you can type:

    grep inputs. /etc/telegraf/telegraf.conf.orig 
https://github.com/influxdata/telegraf/tree/master/plugins/inputs

Then the outputs, which is our InfluxDB database:

    [[outputs.influxdb]]
        database = "telegraf"
        urls = [ "http://127.0.0.1:8086" ]
        username = "telegraf"
        password = "Password12!"

Then we can restart telegraf and the metrics will begin to be collected and sent to InfluxDB.

    service telegraf restart

    > use telegraf
    Using database telegraf
    > SELECT * FROM processes LIMIT 5
    name: processes
    time                blocked dead host   idle paging running sleeping stopped total total_threads unknown zombies
    ----                ------- ---- ----   ---- ------ ------- -------- ------- ----- ------------- ------- -------
    1522362620000000000 0       0    nagisa 0    0      5       29       0       35    85            0       1
    1522362630000000000 1       0    nagisa 0    0      1       30       0       32    82            0       0
    1522362640000000000 1       0    nagisa 0    0      1       30       0       32    83            0       0
    1522362650000000000 0       0    nagisa 0    0      1       27       0       28    80            0       0
    1522362660000000000 0       0    nagisa 0    0      1       27       0       28    80            0       0

You can see what Telegraf collects with this command:

    telegraf -test -config /etc/telegraf/telegraf.conf

This is very useful when adding new plugins:
    
    root@server ~# telegraf -test -config /etc/telegraf/telegraf.conf --input-filter cpu
    * Plugin: inputs.cpu, Collection 1
    * Plugin: inputs.cpu, Collection 2
    > cpu,cpu=cpu0,host=server usage_user=1.9999999999527063,usage_system=0,usage_idle=97.99999999813735,usage_iowait=0,usage_steal=0,usage_guest=0,usage_nice=0,usage_irq=0,usage_softirq=0,usage_guest_nice=0 1522576796000000000
    > cpu,cpu=cpu-total,host=nagisa usage_steal=0,usage_user=1.9999999999527063,usage_nice=0,usage_irq=0,usage_softirq=0,usage_guest=0,usage_guest_nice=0,usage_system=0,usage_idle=97.99999999813735,usage_iowait=0 1522576796000000000

### 3. Grafana installation
Grafana is the web app that we will plug to InfluxDB to visualize the data. We will install Grafana using their APT repo, as described in http://docs.grafana.org/installation/debian/.

    # echo "deb https://packagecloud.io/grafana/stable/debian/ stretch main" > /etc/apt/sources.list.d/grafana.list
    # curl https://packagecloud.io/gpg.key | sudo apt-key add -
    # apt install apt-transport-https
    # apt update
    # apt install grafana

The configuration takes place in /etc/grafana/grafana.ini. The defaults are fine and Grafana will use SQLite to store its data. Though, here is what I recommend to change:

    http_addr = 127.0.0.1
    domain = grafana.domain.tld
    enable_gzip = true
    root_url = https://grafana.domain.tld

Then we restart Grafana and we enable it at boot:

    service grafana-server restart
    systemctl enable grafana-server

admin /admin
Password12!




influxdb
SHOW DATABASES
SHOW MEASUREMENTS
SHOW FIELD KEYS
SHOW SERIES
DROP SERIES FROM /.*/


telegraf -test -config /etc/telegraf/telegraf.conf

sudo systemctl start telegraf
sudo systemctl restart telegraf
systemctl status telegraf

Интерфейс доступен по адресу http://myserver.ru:3000.
Логин: admin, пароль: admin.
Изначально в интерфейсе ничего не будет, потому что графана ничего не знает о данных.
Нужно зайти в источники и указать influxdb (бд: telegraf)
Нужно создать свой дашборд с нужными метриками (уйдёт очень много времени) или импортировать уже готовый, например:
928 — позволяет видеть все метрики по выбранному хосту
914 — тоже самое
61 — позволяет метрики по выбранным хостам на одном графике
Grafana имеет отличный инструмент для импорта сторонних дашбордов (достаточно указать его номер), вы также можете создать свой дашборд и поделиться им с сообществом.
Вот список всех дашбордов, работающие с данными из influxdb, которые были собраны с помощью коллектора telegraf.