from abc import ABC, abstractmethod


class MQTTSubscriber(ABC):
    @abstractmethod
    def set_client(self):
        pass

    @abstractmethod
    def connect(self, mqtt_client, broker_address, broker_port):
        pass

    @abstractmethod
    def set_on_connect(self, mqtt_client, on_connect_func):
        pass

    @abstractmethod
    def set_on_message(self, mqtt_client, on_message_func):
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
