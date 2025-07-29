import threading
import subprocess
import sys
import os

def run_interface():
    os.chdir(os.path.join(os.path.dirname(__file__), "src"))
    # Lance interface.py dans un thread
    def target():
        os.system(f"{sys.executable} interface.py")
    t = threading.Thread(target=target)
    t.daemon = True
    t.start()

def run_proxy():
    # Chemin absolu vers mitmproxy.exe (à adapter selon ton installation)
    mitmproxy_path = r"C:\Users\andra\AppData\Local\Programs\Python\Python311\Scripts\mitmproxy.exe"
    if not os.path.exists(mitmproxy_path):
        print("Erreur : mitmproxy n'est pas installé à l'emplacement spécifié.")
        return
    # Lance mitmproxy sur 0.0.0.0:8080
    subprocess.run([mitmproxy_path, "--listen-host", "0.0.0.0", "--listen-port", "8080"])

if __name__ == "__main__":
    run_interface()
    run_proxy()
