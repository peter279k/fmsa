from openant.easy.node import Node
from abc import ABC, abstractmethod
from openant.devices.scanner import Scanner
from openant.devices import ANTPLUS_NETWORK_KEY


class ANTScanner(ABC):
    @abstractmethod
    def scan(self, file_path=None, device_id=0, device_type=0, auto_create=False):
        devices = []

        node = Node()
        node.set_network_key(0x00, ANTPLUS_NETWORK_KEY)
        scanner = Scanner(node, device_id=device_id, device_type=device_type)

        return scanner

class BluetoothScanner(ABC):
    @abstractmethod
    def start_scan(self):
        pass

    @abstractmethod
    def stop_scan(self):
        pass

class Connect(ABC):
    @abstractmethod
    def connect(self):
        pass

class Disconnect(ABC):
    @abstractmethod
    def disconnect(self):
        pass
