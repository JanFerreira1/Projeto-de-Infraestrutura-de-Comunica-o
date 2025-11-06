# main.py
from analyzer import EthernetAnalyzer

def main():
    print("=== Analisador de Pacotes Ethernet - MODO SCAPY ===")
    analyzer = EthernetAnalyzer()

    # ------------------------------------------------------------------
    # Substitua AQUI:
    interface_de_rede = "Intel(R) Wireless-AC 9462" 
    pacotes_a_capturar = 5 # Vamos tentar 5 pacotes para começar
    # ------------------------------------------------------------------

    # Inicia a captura e análise em tempo real
    analyzer.start_capture(iface=interface_de_rede, count=pacotes_a_capturar)

if __name__ == "__main__":
    main()
