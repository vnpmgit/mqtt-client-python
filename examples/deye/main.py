import logging

from constants import kaa_kpc_host, kaa_kpc_port, token, app_version, tenant_id, app_name
from kaa_mqtt_client import KaaMqttClient
from inverter import get_metadata
from deye_client import DeyeClient
from kaa_mqtt_client.utils.dashboard import process_dashboards

def run_endpoint(kpc_host, kpc_port, app_version, token, metadata, update_interval):
    kaa_client = KaaMqttClient(host=kpc_host, port=kpc_port, application_version=app_version, token=token, client_id='counter')
    kaa_client.connect()

    sys_scan_client = DeyeClient(kaa_client, metadata, update_interval)

    print(f"Connected to Kaa at {kpc_host}:{kpc_port} with app version {app_version} and token {token}")
    while sys_scan_client.is_running:
        sys_scan_client.step()


def main():
    process_dashboards(tenant_id, app_version, app_name, './template/raw/', './template/output/')
    metadata = get_metadata()
    run_endpoint(kaa_kpc_host, kaa_kpc_port, app_version, token, metadata, 120)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    main()
