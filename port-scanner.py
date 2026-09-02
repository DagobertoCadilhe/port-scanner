import socket
import time

common_ports = {
    20: "FTP-data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP-server",
    68: "DHCP-client",
    69: "TFTP",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    123: "NTP",
    135: "MSRPC",
    137: "NetBIOS-ns",
    138: "NetBIOS-dgm",
    139: "NetBIOS-ssn",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP-trap",
    179: "BGP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    464: "Kerberos-change",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD",
    587: "SMTP-submission",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
} 

def scan_ports(host: str, port:int) -> tuple[bool, int, float]:
  """
  Tenta connectar ao IP informado com as portas em common_ports.
  Retorna uma tupla de (is_opened, error_code)
  """

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.settimeout(1)

    start_time = time.time()
    result = s.connect_ex((host, port))
    finish_time = time.time()

    elapsed_time = (finish_time - start_time)
    is_open = (result == 0)

    return((is_open, result, elapsed_time))

def main():

  status = "None"
  host = "8.8.8.8"

  print(f"Starting Port Scan at : {host}")

  for port, port_name in common_ports.items():
    is_opened, error_code, duration = scan_ports(port=port, host=host)

    status = "OPENED" if is_opened else "CLOSED"
    print(f"Port {port:2d} ({port_name:11s}): {status} | Return: {error_code} | Time: {duration:.2f}s")
  

if __name__ == "__main__":
  main()