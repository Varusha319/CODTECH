import socket
import threading
def port_scanner(host, ports=[21, 22, 23, 25, 53, 80, 443, 8080]):
    print(f"\n🔍 Scanning ports on {host}...")
    open_ports = []
    def scan(port):
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((host, port))
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        except:
            pass
        finally:
            s.close()
    threads = []
    for port in ports:
        t = threading.Thread(target=scan, args=(port,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return open_ports
def brute_force_simulation(usernames, passwords):
    print("\n🛡️ Simulated Brute Force Attack:")
    target_username = "admin"
    target_password = "1234"
    for username in usernames:
        for password in passwords:
            print(f"Trying: {username}:{password}")
            if username == target_username and password == target_password:
                print(f"🔓 Match found! Username: {username}, Password: {password}")
                return
    print("❌ No credentials matched.")
if __name__ == "__main__":
    target_host = input("Enter the target IP/Host: ")
    port_scanner(target_host)
    usernames = ["admin", "user", "test"]
    passwords = ["123", "1234", "admin"]
    brute_force_simulation(usernames, passwords)