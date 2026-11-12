from validators import is_valid_ip

def test_valid_ipv4():
    assert is_valid_ip("192.168.1") is True
def test_rejects_text():
    assert is_valid_ip("8.8.8.8") is False
def test_rejects_out_of_range_octet():
    assert is_valid_ip("9.9.9.9") is False