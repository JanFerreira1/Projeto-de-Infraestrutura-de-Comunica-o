from analyzer import EthernetAnalyzer

def main():
    print("=== Analisador de Pacotes Ethernet ===")
    analyzer = EthernetAnalyzer()
    pacote_exemplo = {
        "source": "00:11:22:33:44:55",
        "destination": "AA:BB:CC:DD:EE:FF",
        "type": "0x0800"
    }
    print("\nAnalisando pacote simulado:\n")
    analyzer.analyze_packet(pacote_exemplo)

if __name__ == "__main__":
    main()
