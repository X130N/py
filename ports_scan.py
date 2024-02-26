import socket
import ipaddress
import progressbar


def valida_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False
    
def valida_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False

def scan_ports(ip, port_range):
    open_ports = []
    total_ports = len(port_range)
    
    with progressbar.ProgressBar(max_value=total_ports) as bar:
        for port in port_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            result = sock.connect_ex((ip, port))
            
            if (result == 0):
                open_ports.append(port)
                
            bar.update(port)
            
            sock.close()
            
    return open_ports

def main():
    ip = input("Digite um endereço IP para o scan: ")
    
    if(valida_ipv4(ip) or valida_ipv6(ip)):
        print("Endereço IP válido. ")
    else:
        print("Endereço IP invalido. ")
        return
    
    port_range = range(1,1025)
    
    open_ports = scan_ports(ip, port_range)
    
    if(open_ports):
        print(f"\nPOrtas abertas em {ip}: {', '.join(map(str, open_ports))}")
    else:
        print(f"\nNenhuma porta aberta encontrada em {ip}.")
        
if __name__ == "__main__":
    main()