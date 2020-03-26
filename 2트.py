from scapy.all import *

global a
a=0

def sh(pkt) :
    global a
    a+=1

    src=pkt[0][0].src
    dst=pkt[0][0].dst

    print(a,'번째 패킷','\nsrc MAC=',src,'\ndst MAC=',dst,'\n')

sniff(count=2, prn=sh, filter='arp')
