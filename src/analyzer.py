# analyzer.py
from packet import Packet
from scapy.all import sniff
from scapy.layers.l2 import Ether
from utils import append_packet_log

class EthernetAnalyzer:
    def __init__(self):
        print("Analisador Ethernet inicializado (pronto para Scapy).")

    def analyze_scapy_packet(self, scapy_packet):
        """
        Analisa um pacote REAL do Scapy e salva nos logs usando nossa classe Packet.
        """
        try:
            # Garantir que o pacote tem camada Ethernet (Camada 2)
            if Ether in scapy_packet:
                eth_layer = scapy_packet[Ether]

                # Extrai dados do scapy
                packet_data = {
                    "source": eth_layer.src,
                    "destination": eth_layer.dst,
                    "type": hex(eth_layer.type)
                }

                # Cria nosso objeto Packet
                packet = Packet(
                    source_mac=packet_data["source"],
                    destination_mac=packet_data["destination"],
                    eth_type=packet_data["type"]
                )

                # Exibe no terminal
                print("-" * 40)
                print(f"Pacote Capturado: {packet}")
                print("-" * 40)

                # Salva no log
                append_packet_log({
                    "source": packet.source_mac,
                    "destination": packet.destination_mac,
                    "eth_type": packet.eth_type
                })

        except Exception as e:
            print(f"[ERRO] Falha ao analisar pacote: {e}")

    def start_capture(self, iface="Intel(R) Wireless-AC 9462", count=5, bpf_filter="ether"):
        """
        Inicia a captura de pacotes com filtro BPF.
        """
        print(f"\nIniciando captura na interface '{iface}'...")
        print(f"Aguardando {count} pacote(s) | Filtro: '{bpf_filter}'\n")

        try:
            sniff(
                iface=iface,
                count=count,
                prn=self.analyze_scapy_packet,
                filter=bpf_filter,
                store=0
            )

        except PermissionError:
            print("\n[ERRO] Permissão negada!")
            print("Execute o programa como ADMINISTRADOR (Windows) ou com sudo (Linux).")

        except OSError as e:
            print(f"\n[ERRO] Interface inválida ou inacessível: {iface}")
            print(f"Sistema retornou: {e}")

        except KeyboardInterrupt:
            print("\n[INFO] Captura interrompida pelo usuário (Ctrl+C).")

        except Exception as e:
            print(f"\n[ERRO INESPERADO] {e}")

        finally:
            print("Captura finalizada.")

