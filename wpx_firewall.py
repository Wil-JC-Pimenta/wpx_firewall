#!/usr/bin/env python3
import os
import sys
from datetime import datetime
from scapy.all import sniff
from scapy.layers.inet import IP
import json
import threading
from pathlib import Path
import signal
import time

class WPXFirewall:
    def __init__(self):
        self.blacklist = set()
        self.blacklist_file = "blacklist.json"
        self.log_file = "firewall.log"
        self.running = True
        self.scanning = False
        self.capture_thread = None
        self._load_blacklist()
        self._setup_logging()
        
    def _setup_logging(self):
        """Configure logging system."""
        if not os.path.exists('logs'):
            os.makedirs('logs')
        self.log_path = Path('logs') / self.log_file

    def _load_blacklist(self):
        """Load blacklist from JSON file."""
        try:
            if os.path.exists(self.blacklist_file):
                with open(self.blacklist_file, 'r') as f:
                    self.blacklist = set(json.load(f))
        except Exception as e:
            self._log_event(f"Error loading blacklist: {str(e)}")
            self.blacklist = set()

    def _save_blacklist(self):
        """Save blacklist to JSON file."""
        try:
            with open(self.blacklist_file, 'w') as f:
                json.dump(list(self.blacklist), f)
        except Exception as e:
            self._log_event(f"Error saving blacklist: {str(e)}")

    def add_to_blacklist(self, ip):
        """Add an IP to the blacklist."""
        self.blacklist.add(ip)
        self._save_blacklist()
        self._log_event(f"IP {ip} added to blacklist")
        print(f"\n[+] IP {ip} has been added to the blacklist.")

    def remove_from_blacklist(self, ip):
        """Remove an IP from the blacklist."""
        if ip in self.blacklist:
            self.blacklist.remove(ip)
            self._save_blacklist()
            self._log_event(f"IP {ip} removed from blacklist")
            print(f"\n[-] IP {ip} has been removed from the blacklist.")
        else:
            print(f"\n[!] IP {ip} is not in the blacklist.")

    def _log_event(self, message):
        """Log events to file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        try:
            with open(self.log_path, 'a') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Error writing to log: {str(e)}")

    def packet_handler(self, packet):
        """Process captured packets."""
        if not self.scanning:
            return
        if IP in packet:
            src_ip = packet[IP].src
            if src_ip in self.blacklist:
                self._log_event(f"Packet blocked from IP: {src_ip}")
                return
            return packet

    def stop(self):
        """Stop the firewall."""
        self.running = False
        self.scanning = False
        self._log_event("Firewall stopped")
        print("\n[*] Firewall stopped.")
        os._exit(0)

    def toggle_scanning(self):
        """Toggle packet scanning on/off."""
        self.scanning = not self.scanning
        status = "started" if self.scanning else "paused"
        print(f"\n[*] Packet scanning {status}")
        self._log_event(f"Packet scanning {status}")

    def start_packet_capture(self):
        """Start packet capture in a separate thread."""
        try:
            self._log_event("Firewall started")
            sniff(prn=self.packet_handler, store=0, stop_filter=lambda _: not self.running)
        except Exception as e:
            self._log_event(f"Error during firewall execution: {str(e)}")

    def display_menu(self):
        """Display the interactive menu."""
        menu = """
╔════════════════════════════════════╗
║          WPX Firewall              ║
╠════════════════════════════════════╣
║ 1. Add IP to blacklist             ║
║ 2. Remove IP from blacklist        ║
║ 3. List blocked IPs                ║
║ 4. Toggle packet scanning          ║
║ 5. Quit                            ║
╚════════════════════════════════════╝
"""
        print(menu)

    def list_blocked_ips(self):
        """Display all blocked IPs."""
        if self.blacklist:
            print("\nBlocked IPs:")
            print("═" * 50)
            for ip in sorted(self.blacklist):
                print(f"  • {ip}")
            print("═" * 50)
        else:
            print("\n[!] No IPs are currently blocked.")

    def start(self):
        """Start the firewall with interactive menu."""
        # Start packet capture thread
        self.capture_thread = threading.Thread(target=self.start_packet_capture)
        self.capture_thread.daemon = True
        self.capture_thread.start()

        print("\n[*] Firewall started. Packet scanning is paused.")
        print("[*] Current blocked IPs:")
        self.list_blocked_ips()
        
        while self.running:
            try:
                self.display_menu()
                choice = input("\nEnter your choice (1-5): ").strip()

                if choice == "1":
                    ip = input("Enter IP to block: ").strip()
                    self.add_to_blacklist(ip)
                
                elif choice == "2":
                    ip = input("Enter IP to unblock: ").strip()
                    self.remove_from_blacklist(ip)
                
                elif choice == "3":
                    self.list_blocked_ips()
                
                elif choice == "4":
                    self.toggle_scanning()
                
                elif choice == "5":
                    print("\n[*] Shutting down firewall...")
                    self.stop()
                    break
                
                else:
                    print("\n[!] Invalid choice. Please try again.")

                input("\nPress Enter to continue...")
                os.system('cls' if os.name == 'nt' else 'clear')
            
            except KeyboardInterrupt:
                print("\n[!] Shutting down firewall...")
                self.stop()
                break
            except Exception as e:
                print(f"\n[!] Error: {str(e)}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("╔════════════════════════════════════╗")
    print("║     Starting WPX Firewall          ║")
    print("╚════════════════════════════════════╝")
    
    firewall = WPXFirewall()
    
    # Configure CTRL+C handler
    def signal_handler(signum, frame):
        print("\n[!] Shutting down firewall...")
        firewall.stop()
    
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start the firewall
    firewall.start()

if __name__ == "__main__":
    main() 