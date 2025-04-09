import json
from abc import ABC, abstractmethod


class MQTTPublisher(ABC):
    @abstractmethod
    def create_client(self):
        pass

    @abstractmethod
    def connect(self, mqtt_client, broker_address, broker_port):
        pass

    @abstractmethod
    def set_on_connect(self, mqtt_client, on_connect_func):
        pass

    @abstractmethod
    def set_username_pw(self, mqtt_client, username, password):
        pass

    @abstractmethod
    def set_tls_cert_path(self, mqtt_client, broker_cert_path):
        pass

    @abstractmethod
    def set_insecure_tls(self, mqtt_client, is_insecure):
        pass

class MQTTSinglePublisher(ABC):
    @abstractmethod
    def publish_single(self, mqtt_publisher):
        mqtt_publisher.single(
            topic=self.mac_address,
            payload=json.dumps(self.payload),
            qos=0,
            retain=False,
            hostname=self.mqtt_config['host'],
            port=self.mqtt_config['port'],
            client_id='',
            keepalive=60,
            will=None,
            auth={'username': self.mqtt_config['user'], 'password': self.mqtt_config['password']},
            tls={'ca_certs': self.mqtt_config['ca_path'], 'insecure': True},
            transport='tcp'
        )

    @abstractmethod
    def set_mac_address(self, mac_address):
        self.mac_address = mac_address

    @abstractmethod
    def set_payload(self, payload):
        self.payload = payload
