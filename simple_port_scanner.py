"""
A simple TCP connect port scanner.
Opens a short lived connection to each port in a list and records
which ones accept the connection. This is the same technique a
basic network scan is built on.
"""

import socket
from datetime import datetime

class PortScanner:
#  Scans a single target for a list of open TCP ports.
    def __init__(
    self, target: str, ports: list[int], timeout: float = 0.5
    ) -> None:
        self.target = target
        self.ports = ports
        self.timeout = timeout
        self.open_ports: list[int] = []
    
    
    def scan(self) -> list[int]:
        # Check every configured port and return the ones that are open.
        for port in self.ports:
            if self._is_open(port):
                self.open_ports.append(port)
            return self.open_ports
    
    def _is_open(self, port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(self.timeout)
        try:
            result = sock.connect_ex((self.target, port))
            return result == 0
        except socket.gaierror:
            raise ValueError(f"Could not resolve host: {self.target}")
    
    
    def report(self) -> None:
        # Print a short, readable summary of the scan.
        now = datetime.now().strftime('%H:%M:%S')
        print(f"Scan of {self.target} completed at {now}")
        if not self.open_ports:
            print("No open ports found.")
            return
        for port in self.open_ports:
            print(f" {port}/tcp open")


if __name__ == "__main__":
    ports = [21, 22, 80, 443, 3389, 0, 90, 8, 7, 6 ,500, 77, 80, 89, 45, 53, 67, 10, 40, 50]
    scanner = PortScanner(target="172.27.125.219", ports=ports)
    scanner.scan()
    scanner.report()
