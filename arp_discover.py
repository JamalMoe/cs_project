"""Discover live hosts on a local subnet using ARP requests."""


from scapy.all import ARP, Ether, srp

def arp_scan(ip_range: str) -> list[dict]:
    """Send an ARP request to every address in ip_range and return replies."""
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request
    answered, _ = srp(packet, timeout=2, verbose=False)
    return [{"ip": r.psrc, "mac": r.hwsrc} for _, r in answered]

if __name__ == "__main__":
    s = arp_scan("192.168.0.159/24")
    print(f"{'IP':<16}{'MAC'}")
    for device in s:
        print(f"{device['ip']:<16}{device['mac']}")
