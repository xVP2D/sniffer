import subprocess

def start_mitmproxy():
    # Lance mitmproxy en mode transparent sur 0.0.0.0:8080
    cmd = [
        "mitmproxy",
        "--listen-host", "0.0.0.0",
        "--listen-port", "8080"
    ]
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("Erreur : mitmproxy n'est pas installé.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du lancement de mitmproxy : {e}")

if __name__ == "__main__":
    start_mitmproxy()