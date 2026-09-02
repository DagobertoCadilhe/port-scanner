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
    7:  "Echo",
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

    elapsed_time = (start_time - finish_time)
    is_open = (result == 0)

    return((is_open, result, elapsed_time))

  if not success == 0:
    print(f"Port {port} : {port_name}, is opened", end="")
    print(f" Return {success} & Time {(timef - times ):.1f}ms")
  else:
    print(f"Port {port} : {port_name}, is closed", end ="")
    print(f" Return {success} & Time {(timef - times ):.1f}ms")


def main():

  status = "None"
  host = "8.8.8.8"

  for port, port_name in common_ports.items():
    is_opened, error_code, duration = scan_ports(port=port, host=host)

    status = "OPENED" if is_opened else "CLOSED"
    print(f"Port {port:2d} ({port_name:11s}): {status} | Return: {error_code} | Time: {duration:.2f}s")
  

if __name__ == "__main__":
  main()