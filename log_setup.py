"""Shared logging configuration for every SentinelKit module."""

import logging
import yaml

def load_config(path: str = "config.yaml") -> dict:
    with open(path) as f:
        return yaml.safe_load(f)

def setup_logging(config: dict) -> None:
    log_config = config["logging"]
    logging.basicConfig(
        filename=log_config["file"],
        level=getattr(logging, log_config["level"]),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
