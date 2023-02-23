# <em> InfluxDocs </em>
Proporcionar documentación para instalación y uso de InfluxDB

## Instalación

### InfluxDB OSS

#### Docker Image

[Hacer clic aquí para iniciar a usar docker](https://www.docker.com/get-started/)
Es recomendable usar una cuenta de docker hub

```Docker Image
docker pull influxdb:2.6.1
```
Cambiamos (container_name) por el nombre que deseemos ponerle al contenedor. El modificador (-p) es para seleccionar el puerto el cual se lo transmitirá para entrar en el navegador al gestor de Influx. (-d) ejecuta influxdb en segundo plano.
```
docker run --name container_name -p 8086:8086 -d influxdb
```
Para hacer que la bases de datos manajadas con influx. Se guarden en almacenamiento a parte del contenedor de Docker. 
```
docker run --name nombre_del_contenedor -p 8086:8086 -v /ruta/a/mis/datos:/var/lib/influxdb -d influxdb
```
Para correr el Influx CLI en mi contenedor de Docker. El modificador (-it) ejecuta el contenedor con una terminal interactiva en este caso para el InfluxDB CLI.
```
docker exec -it nombre_del_contenedor influx
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

## Recomendación a la hora de seguir la documentación oficial:
### Cuando ejecutamos los pasos anteriores estamos descargando e instalando la versión 2.x de Influxdb OSS lo cual puede llevar a confusiones para usar los comando del Influx CLI pues cambia la forma de crear bases de datos con respecto a la versión de Influx CLI 1.x a continuación enlaces a la documentación oficial para seguir la estructura de comando en caso de querer usar el CLI.
## Documantacion oficial de Influxdb para el uso de comando en el CLI:
* ### [Proveer las credenciales](https://docs.influxdata.com/influxdb/v2.6/reference/cli/influx/#provide-required-authentication-credentials) Se puede contar con diversas configuraciones en caso de tener múltiples organizaciones o estar corriendo InfluxDB OSS en otro puerto o un url proporcionado por un proveedor de cómputo en la nube.
* ### [Crear una organizacion](https://docs.influxdata.com/influxdb/v2.6/organizations/create-org/) en caso de tener múltiples organizaciones donde alguna no tiene acceso al bucket que pertenece a otra.
* ### [Crear un bucket](https://docs.influxdata.com/influxdb/v2.6/reference/cli/influx/bucket/create/) Los bucket son la base de datos en la cual se va a suministrar la data.
* ### [Crear un token](https://docs.influxdata.com/influxdb/cloud/security/tokens/create-token/)
* ### [URLS Custom](https://docs.influxdata.com/influxdb/v2.6/reference/urls/)
* ### [Cargar informacion al Bucket](https://docs.influxdata.com/influxdb/cloud/write-data/no-code/load-data/)
* ### [Escribir infomacion en la base de datos](https://docs.influxdata.com/influxdb/v2.6/write-data/developer-tools/influx-cli/)
