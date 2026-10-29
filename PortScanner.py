import socket


IP = (input('Input target IP address: '))

ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 123, 135, 137, 139, 143, 161, 389, 443, 445, 465, 587, 636, 993, 995, 1433, 1521, 1723, 3306, 3389, 5432, 5900, 5985, 5986, 6379, 8080, 8443, 9200, 27017]


def check_port(IP, port):
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((IP, port))
    sock.close()
    return result


for port in ports:
   result = check_port(IP, port)

   if result == 0:
      print(f'Port {port} is open')
   else: print(f'Port {port} is not confirmed')