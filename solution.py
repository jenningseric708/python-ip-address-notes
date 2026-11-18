import ipaddress

def solve(value):
    return (lambda a: {"version": a.version, "compressed": a.compressed, "loopback": a.is_loopback})(ipaddress.ip_address(value))
