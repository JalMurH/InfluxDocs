from influxdb_client import InfluxDBClient

class InfluxDB:
    def __init__(self, url: str, token: str, org: str, bucket: str) -> None:
        self._client = InfluxDBClient(url=url, token=token)
        self._org = org
        self._bucket = bucket
    
    def write(self, data: dict) -> None:
        write_api = self._client.write_api()
        write_api.write(bucket=self._bucket, org=self._org, record=data)
        write_api.close()
    
    def query(self, query: str) -> list:
        query_api = self._client.query_api()
        result = query_api.query(query=query, org=self._org)
        return list(result)