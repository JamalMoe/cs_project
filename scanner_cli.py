"""Command line interface for the threaded port scanner."""

import argparse
import json
from multithreading import threaded_scan


def parse_ports(port_string: str) -> list[int]:
    """Convert a string like '1-100' or '22,80,443' into a list of ints."""
    if "-" in port_string:
        start, end = port_string.split("-")
        return list(range(int(start), int(end) + 1))
    return [int(p) for p in port_string.split(",")]

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scanner_cli",
        description="A threaded TCP port scanner for authorised targets only.",
    )

    parser.add_argument("target", help="IP address or hostname to scan")
    parser.add_argument(
        "-p", "--ports", default="1-1024",
        help="Port range or comma separated list, default 1-1024",
    )

    parser.add_argument(
        "-t", "--threads", type=int, default=100,
        help="Number of worker threads, default 100",
    )

    parser.add_argument("-o", "--output", help="Save results as JSON to this file")
    return parser

if __name__ == "__main__":
    args = build_parser().parse_args()
    ports = parse_ports(args.ports)
    msg = f"Scanning {args.target}, {len(ports)} ports, {args.threads} threads"
    print(msg)
    open_ports = threaded_scan(args.target, ports, max_threads=args.threads)
    print(f"Open ports: {open_ports}")
    
    if args.output:
        results = {"target": args.target, "open_ports": open_ports}
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {args.output}")
