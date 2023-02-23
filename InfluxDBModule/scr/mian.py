from data import InfluxDB

if __name__ == "__main__":
    url = "http://influxdb:8086"
    token = "my_admin_token"
    org = "my_org"
    bucket = "my_bucket"
    
    influx = InfluxDB(url=url, token=token, org=org, bucket=bucket)
    
    # Ejemplo de escritura de datos
    data = {"measurement": "example_measurement", "tags": {"tag1": "value1"}, "fields": {"field1": 123.45}}
    influx.write(data)
    
    # Ejemplo de consulta de datos
    query = 'from(bucket:"my_bucket") |> range(start:-1h)'
    results = influx.query(query)
    print(results)
