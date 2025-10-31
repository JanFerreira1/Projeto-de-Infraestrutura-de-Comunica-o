from packet import Packet

class EthernetAnalyzer:
    def __init__(self):
        print("Analisador Ethernet inicializado (modo esqueleto).")

    def analyze_packet(self, packet_data):
        try:
            packet = Packet(
                source_mac=packet_data["source"],
                destination_mac=packet_data["destination"],
                eth_type=packet_data["type"]
            )
            print(packet)
        except Exception as e:
            print(f"Erro ao analisar pacote: {e}")
