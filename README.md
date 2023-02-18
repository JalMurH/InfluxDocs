# <em> InfluxDocs </em>
Proporcionar Documentacion para instalacion y uso de InfluxDB

## Instalacion

### InfluxDB OSS

#### Docker Image

[Hacer clic aqui para iniciar a usar docker](https://www.docker.com/get-started/)
Es recomendable usar una cuanta de docker hub

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
wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.6.1-linux-amd64.tar.gz
```
Descomprimimos el archivo descargado

```
tar xvfz influxdb2-2.6.1-linux-amd64.tar.gz
```
Movemos el archivo descomprimido a (/usr/local/bin) 

```
sudo cp influxdb2-client-latest-linux-amd64/influx /usr/local/bin/
```
## Listos para crear buckets y añadir las series de tiempo a estas.
ingresar al navegador http://localhost:8086

## Recomendacion a la hora de seguir la documentacion oficial:
### Cuando ejecutamos los pasos anteriores estamos descargando e instalando la version 2.x de Influxdb OSS lo cual puede llavar a confuciones para usar los comando del Influx CLI pues cambia la forma de crear bases de datos conrespecto a la version de Influx CLI 1.x a continuacion enlaces a la documentacion oficial para segir la estructura de comando en caso de querer usar el CLI.
## Documantacion oficial de Influxdb para el uso de comando en el CLI:
* ### [Probeer las credenciales](https://docs.influxdata.com/influxdb/v2.6/reference/cli/influx/#provide-required-authentication-credentials) Sepuede contar con diversas configuraciones en caso de tener multiples organizaciones o estar corrinedo InfluxDB OSS en otro puerto o un url porporcionado por un probeedor de computo en la nube.
* ### [Crear una organizacion](https://docs.influxdata.com/influxdb/v2.6/organizations/create-org/) en caso de tener multiples organizaciones donde alguna no tiene acceso al bucket que pertenece a otra.
