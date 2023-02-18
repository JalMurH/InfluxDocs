#InfluxDocs
Documentacion para instalacion y uso de InfluxDB

# InfluxDocs
Proporcionar Documentacion para instalacion y uso de InfluxDB

## Instalacion

### InfluxDB OSS

#### Docker Image

```Docker Image
docker pull influxdb:2.6.1
```
Cambiamos (container_name) por el nombre que deseemos ponerle al contenedor. el modificador (-p) es para seleccionar el puerto el cual se va transmitir para entrar en el navegador al gestor de Influx. (-d) ejecuta influxdb en segundo plano.
```
docker run --name container_name -p 8086:8086 -d influxdb
```

#### Linux
Descargamos InfluxDB OSS (wget descarga los archivos a los que llaman binarios)

```Linux 
wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.6.1-linux-arm64.tar.gz
```
Descomprimimos el archivo descargado

```
tar xvfz influxdb2-2.6.1-linux-arm64.tar.gz
```
Movemos el archivo descomprimido a (/usr/local/bin) 

```
sudo cp influxdb2-client-latest-linux-amd64/influx /usr/local/bin/
```
## Listos para crear buckets y añadir las series de tiempo a estas.
ingresar al navegador http://localhost:8086
