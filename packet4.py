import socket, sys

from struct import *

source_ip = '192.168.159.129'

dest_ip = '192.168.10.128' # or socket.gethostbyname('www.google.com')

#create a raw socket

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

except socket.error , msg:

    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]

    sys.exit() 

    # tell kernel not to put in headers, since we are providing it, when using IPPROTO_RAW this is not necessary

    # s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    # now start constructing the packet

    packet = '';
# ip header fields

ip_ihl = 5

ip_ver = 4

ip_tos = 0

ip_tot_len = 0  # kernel will fill the correct total length

ip_id = 54321   #Id of this packet

ip_frag_off = 0

ip_ttl = 255

ip_proto = socket.IPPROTO_UDP

ip_check = 0    # kernel will fill the correct checksum

ip_saddr = socket.inet_aton ( source_ip )   #Spoof the source ip address if you want to

ip_daddr = socket.inet_aton ( dest_ip )

ip_ihl_ver = (4 << 4) | 5

# the ! in the pack format string means network order

ip_header = pack('!BBHHHBBH4s4s' , ip_ihl_ver, ip_tos, ip_tot_len, ip_id, ip_frag_off, ip_ttl, ip_proto, ip_check, ip_saddr, ip_daddr)

user_data = 'Hello, how are you'

# pseudo header fields

source_address = socket.inet_aton( source_ip )

dest_address = socket.inet_aton(dest_ip)

placeholder = 0
protocol = socket.IPPROTO_UDP

length = len(user_data)

psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol,length);

psh = psh + user_data;

# final full packet - syn packets dont have any data

packet = ip_header + user_data

#Send the packet finally - the port specified has no effect
var = 1
while var == 1:
    s.sendto(packet, (dest_ip , 0 ))
    print "Sending",(s.sendto(packet,(dest_ip,0))),"bytes"
