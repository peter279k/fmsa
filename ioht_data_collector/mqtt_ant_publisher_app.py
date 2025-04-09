import os
import time
import sqlite3
import configparser
import paho.mqtt.client as mqtt
from config.ConfigLoader import ConfigLoader
from interfaces.Publisher import MQTTSinglePublisher


class ANTConnector:
    pass


class Publisher(MQTTSinglePublisher, ConfigLoader):
    def load_config(self, config_path, allowed_sections, allowed_keys):
        if os.path.isfile(config_path) is False:
            raise FileNotFoundError(f'{config_path} file is not found.')

        config_parser = configparser.ConfigParser()
        config_parser.read(config_path)

        sections = config_parser.sections()

        for allowed_section in allowed_sections:
            if allowed_section not in sections:
                raise KeyError(f'{allowed_section} is not found.')

        for allowed_mqtt_key in allowed_keys:
            if allowed_mqtt_key not in config_parser[allowed_sections[0]]:
                raise KeyError(f'{allowed_mqtt_key} is not found.')

        mqtt_host = config_parser[allowed_sections[0]]['host'].replace('"', '')
        mqtt_port = int(config_parser[allowed_sections[0]]['port'].replace('"', ''))
        mqtt_user = config_parser[allowed_sections[0]]['user'].replace('"', '')
        mqtt_password = config_parser[allowed_sections[0]]['password'].replace('"', '')
        mqtt_ca_path = config_parser[allowed_sections[0]]['ca_path'].replace('"', '')
        sqlite3_db_path = config_parser[allowed_sections[0]]['sqlite3_db'].replace('"', '')

        devices_sql = '''
        SELECT
            id, manufacture_name, device, created,
            name, circumference, qr_code_info, complete_name
        FROM devices
        WHERE complete_name is NOT NULL
        '''
        with sqlite3.connect(sqlite3_db_path) as db:
            result = db.execute(devices_sql)
            rows = result.fetchall()
            result.close()

        mqtt_topics = []
        cyc_connections = []
        for record in rows:
            mqtt_topics += (record[2], 0),
            if record[7] is None:
                continue
            cyc_connections += record[7],

        mqtt_info = {
            'host': mqtt_host,
            'port': mqtt_port,
            'user': mqtt_user,
            'password': mqtt_password,
            'topics': mqtt_topics,
            'ca_path': mqtt_ca_path,
            'cyc_connections': cyc_connections,
        }

        return {
            'mqtt_info': mqtt_info,
        }

def on_connect(mqtt_client, user_data, flags, reason_code, properties):
    if reason_code == 0:
        log_message = f'[{int(time.time())}] Successful connection!'
        print(log_message)
    else:
        log_message = f'[{int(time.time())}] Not able to connect!'
        print(log_message)

        mqtt_client.loop_stop()


if __name__ == '__main__':
    publisher_app = MQTTSinglePublisher()
    configuration = publisher_app.load_config()
    broker_address = configuration['mqtt_info']['host']
    broker_port = configuration['mqtt_info']['port']
    broker_user = configuration['mqtt_info']['user']
    broker_password = configuration['mqtt_info']['password']
    broker_certificate_path = configuration['mqtt_info']['ca_path']
    broker_topics = configuration['mqtt_info']['topics']
    the_cyc_connections = configuration['mqtt_info']['cyc_connections']

    mqtt_client = publisher_app.create_client()

    mqtt_client = publisher_app.set_on_connect(mqtt_client, on_connect)
    mqtt_client = publisher_app.set_username_pw(mqtt_client, broker_user, broker_password)
    mqtt_client = publisher_app.set_tls_cert_path(mqtt_client, broker_certificate_path)
    mqtt_client = publisher_app.set_insecure_tls(mqtt_client, True)
    mqtt_client = publisher_app.connect(
        host=broker_address, port=broker_port
    )
