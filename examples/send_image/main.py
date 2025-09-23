import time
import logging
import uuid
import datetime
from kaa_mqtt_client import KaaMqttClient
from constants import logger, kaa_kpc_host, kaa_kpc_port, app_version, token, kaa_domain_url

class SendImage:
    def __init__(self, client: KaaMqttClient, metadata:dict, update_interval: int = 120):
        self.kaa_client = client
        self.metadata = metadata
        self.update_interval = update_interval
        self.is_running = True

    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: dict):
        if not isinstance(metadata, dict):
            raise Exception("Not supported metadata format")
        if not hasattr(self, "_metadata"):
            self._metadata = metadata
            self._metadata["serial"] = str(uuid.uuid4())
        else:
            self._metadata.update(**metadata)
        self._metadata["lastMaintenance"] = str(datetime.datetime.now())
        self.publish_metadata()

    def publish_metadata(self):
        logger.info(f"Going to publish data sample: {self.metadata}")
        self.kaa_client.publish_metadata(self.metadata)

    def step(self):
        logger.info("Publishing periodic metrics")
        self.kaa_client.publish_binary_file('pic.png', kaa_domain_url)
        
        # self.publish_data_sample(data_sample)
        # time.sleep(self.update_interval)

    def publish_data_sample(self, data):
        logger.info(f"Publishing data sample: {data}")
        self.kaa_client.publish_data_collection(data)
        time.sleep(1)

def run_endpoint(kpc_host, kpc_port, app_version, token, metadata, update_interval):
    kaa_client = KaaMqttClient(host=kpc_host, port=kpc_port, application_version=app_version, token=token, client_id='counter')
    logger.info(f"Connecting to Kaa at {kpc_host}:{kpc_port}...")
    kaa_client.connect()
    time.sleep(3)
    logger.info(f"Connected to Kaa at {kpc_host}:{kpc_port} with app version {app_version} and token {token}")
    


    sendImageClass = SendImage(kaa_client, metadata, update_interval)
    sendImageClass.step()

def main():
    metadata = {
    }
    run_endpoint(kaa_kpc_host, kaa_kpc_port, app_version, token, metadata, 120)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    main()
