from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    protocol = packet[IP].proto

    if packet.haslayer(TCP):
        payload = bytes(packet[TCP].payload)
        protocol_name = "TCP"
    elif packet.haslayer(UDP):
        payload = bytes(packet[UDP].payload)
        protocol_name = "UDP"
    else:
        payload = None
        protocol_name = "Other"


    print(f'Source IP: {source_ip}')
    print(f'Destination IP: {destination_ip}')
    print(f'Protocol: {protocol_name}')
    if payload:
        print(f'Payload: {payload}\n')
    else:
        print('No Payload\n') 

def start_sniffing():
    sniff(prn=packet_callback, filter= "ip", store=0)

if __name__== '__main__':
    print('Sniffing started...')
    start_sniffing()        