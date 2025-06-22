import requests

class ProxyManager:
    def __init__(self):
        self.proxy_list = []
        self.current_proxy = None

    def load_proxies(self, file_path="proxies.txt"):
        try:
            with open(file_path, "r") as f:
                self.proxy_list = [line.strip() for line in f]
            print(f"[+] {len(self.proxy_list)} proxies cargados!")
        except:
            print("[!] No se encontró el archivo de proxies.")

    def rotate_proxies(self):
        if not self.proxy_list:
            self.load_proxies()
        if self.proxy_list:
            self.current_proxy = random.choice(self.proxy_list)
            print(f"[+] Proxy actual: {self.current_proxy}")

    def get_current_proxy(self):
        return self.current_proxy