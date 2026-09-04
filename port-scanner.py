import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

host_ip = "8.8.8.8"

common_ports = {
    7 : "Echo",
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

def scan_ports(host: str, port: int) -> tuple[bool, int]:
  """Escaneia a porta passada e torna se foi possivel se conecatar a ela.
  
  Args:
      host (str): O IP que desejamos ver se a porta está aberta
      port (int): A porta a ser testada sobre o IP passado 
  Returns:
      is_open (bool): Booleano que indica se consegiu comunicar com a porta
      port (int): A porta testada, para ser usada em iteração de prints de resultados
  """
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.settimeout(1)

    result = s.connect_ex((host, port))

    is_open = (result == 0)

    return (is_open, port)

def assync_call(ports: list, host: str):
  """Faz a criação de threads e sua chamada dinamica sobre a lista de portas (common_ports)
     
  Args:
      ports (list): A lista de portas a serem iteradas
      host (str): O IP que desejamos iterar
  Returns:
      results (tuple list): Lista de tuplas onde cada um contem o is_open e port gerados em scan_ports()
  """
  future_list = []

  with ThreadPoolExecutor(max_workers=20) as executioner:
    for port in list(ports):
      future = executioner.submit(scan_ports, host=host, port=port)
      future_list.append(future)

  results = []

  for future in as_completed(future_list):
    port, is_open = future.result()
    results.append((port, is_open))

  return(results)

def main():

  sorted_common_ports = dict(sorted(common_ports.items()))

  start= time.time()
  results = assync_call(ports=common_ports, host=host_ip)
  end = time.time()

  # Ordena as llista de Tuplas em ordem numerica pela segunda key da tupla : key(1)
  sorted_results = sorted(results, key=lambda x: x[1])

  print(f"Starting Port Scan at : {host_ip}")

  for is_open, port in sorted_results:
    if is_open == True : status = "OPENED" 
    else: status = "CLOSED"
    print(f"Port {port:2d} ({sorted_common_ports[port]:11s}): {status}")

  print(f"Port Scan done in {end - start:.2f} seconds")

if __name__ == "__main__":
  main()