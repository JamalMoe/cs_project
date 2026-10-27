import ipaddress
import logging

from log_setup import load_config, setup_logging
from exceptions import ScanTargetError


config = load_config()
setup_logging(config)

logger = logging.getLogger("testingexample.scan")


def scan_target(ip: str) -> None:
    logger.info("Starting scan of %s", ip)

    try:
        # Validate the entire IPv4 address.
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError as exc:
            raise ScanTargetError(
                target=ip,
                reason=f"Invalid IPv4 address: {exc}",
                suggestion="Provide a valid IPv4 address, "
                           "for example 192.168.1.12.",
            ) from exc

        # Scanning logic would go here.
        logger.info("Scan of %s completed successfully", ip)

    except ScanTargetError as exc:
        logger.error("%s", exc)


if __name__ == "__main__":
    scan_target("192.168.1.12")
