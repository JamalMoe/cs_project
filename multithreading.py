# Threaded version of the TCP connect port scanner.

import socket
import time
from concurrent.futures import ThreadPoolExecutor

def check_port(target: str, port: int, timeout: float = 0.5) -> int | None:
    #  Return the port number if open, otherwise None.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        if sock.connect_ex((target, port)) == 0:
            return port
    return None

def threaded_scan( target: str, ports: list[int], max_threads: int = 1024 ) -> list[int]:
    #   Scan every port in parallel and return the ones that are open.
    with ThreadPoolExecutor(max_workers=max_threads) as pool:
        results = pool.map(lambda p: check_port(target, p), ports)
    return sorted(p for p in results if p is not None)


if __name__ == "__main__":
    target = "172.27.125.219"
    ports = list(range(1, 1025))
    start = time.perf_counter()
    open_ports = threaded_scan(target, ports)
    elapsed = time.perf_counter() - start
    print(f"Open ports: {open_ports}")
    print(f"Scanned {len(ports)} ports in {elapsed:.2f} seconds")