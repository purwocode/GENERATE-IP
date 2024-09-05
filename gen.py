import ipaddress

def generate_ips():
    start_ip = ipaddress.IPv4Address('0.0.0.0')
    end_ip = ipaddress.IPv4Address('255.255.255.255')

    current_ip = start_ip
    while current_ip <= end_ip:
        yield str(current_ip)
        current_ip += 1

# Menyimpan IP ke dalam file
with open('ip.txt', 'w') as file:
    for ip in generate_ips():
        file.write(ip + '\n')
