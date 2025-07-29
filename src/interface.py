from flask import Flask, jsonify
import threading

app = Flask(__name__)

# Exemple de stockage des paquets sniffés
sniffed_packets = []

def add_packet(packet):
    sniffed_packets.append(packet)

@app.route('/api/packets', methods=['GET'])
def get_packets():
    return jsonify(sniffed_packets)

def run_flask():
    app.run(host='0.0.0.0', port=5001)

if __name__ == "__main__":
    # Lancer l'API dans un thread séparé
    threading.Thread(target=run_flask).start()