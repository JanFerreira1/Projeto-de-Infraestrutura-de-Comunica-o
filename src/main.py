# main.py

from analyzer import EthernetAnalyzer
from scapy.all import show_interfaces
import sys # Para lidar com a saída e encerramento do script, se necessário

def get_user_interface():
    """
    Lista as interfaces disponíveis e solicita ao usuário que selecione uma.
    Retorna o nome exato da interface.
    """
    print("\n--- Interfaces de Rede Disponíveis ---")
    show_interfaces()
    print("-------------------------------------")
    
    # 1. Pede o nome ao usuário
    interface_name = input("Digite o NOME EXATO da interface para iniciar a captura: ").strip()
    
    # 2. Validação simples para garantir que o usuário digitou algo
    if not interface_name:
        print("\n[ERRO] Nome da interface não pode ser vazio. Encerrando.")
        sys.exit(1) # Sai do programa com erro
        
    return interface_name

def main():
    print("=== Analisador de Pacotes Ethernet - MODO SCAPY ===")
    analyzer = EthernetAnalyzer()
    
    # ------------------------------------------------------------------
    # *** NOVA LÓGICA: SELEÇÃO INTERATIVA ***
    interface_de_rede = get_user_interface()
    
    pacotes_a_capturar = 5 # Manter um padrão para testes
    filtro = "arp"         # Manter o filtro para testes (ou poderia pedir ao usuário também)
    # ------------------------------------------------------------------

    # Inicia a captura usando o nome fornecido pelo usuário
    print(f"\nIniciando captura com interface: {interface_de_rede}")
    analyzer.start_capture(
        iface=interface_de_rede, 
        count=pacotes_a_capturar, 
        bpf_filter=filtro
    )

if __name__ == "__main__":
    main()
