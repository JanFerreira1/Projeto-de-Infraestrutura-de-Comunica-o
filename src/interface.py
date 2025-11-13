# interface.py
import sys
import json
from analyzer import EthernetAnalyzer
from scapy.all import show_interfaces

DEFAULT_CAPTURE_COUNT = 5
DEFAULT_FILTER = "arp"

def clear_screen():
    # funciona em Windows/Linux/Mac
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_interface():
    print("\n--- Interfaces de Rede Disponíveis ---")
    show_interfaces()
    print("-------------------------------------")
    iface = input("Digite o NOME EXATO da interface para iniciar a captura (ou ENTER para cancelar): ").strip()
    return iface

def choose_filter(current_filter):
    print(f"Filtro atual: {current_filter}")
    print("Opções de filtro: ether | arp | ip | ip6")
    f = input("Digite novo filtro (ou ENTER para manter): ").strip()
    return f if f else current_filter

def show_last_captures(logfile="logs/packets.json", n=10):
    try:
        with open(logfile, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("[INFO] Nenhum log encontrado.")
        return
    except json.JSONDecodeError:
        print("[ERRO] arquivo de logs corrompido.")
        return

    print(f"\nÚltimos {n} pacotes (mais recentes primeiro):")
    for pkt in data[-n:][::-1]:
        print(pkt)

def export_logs(format="json", logfile="logs/packets.json"):
    print(f"[INFO] Logs já estão em {logfile} (formato JSON).")
    # aqui poderia implementar CSV caso precise

def main_menu():
    analyzer = EthernetAnalyzer()
    iface = ""
    bpf_filter = DEFAULT_FILTER
    capture_count = DEFAULT_CAPTURE_COUNT

    while True:
        try:
            clear_screen()
            print("=== ANALISADOR ETHERNET - MENU ===")
            print(f"Interface selecionada: {iface or '<nenhuma>'}")
            print(f"Filtro BPF: {bpf_filter}")
            print("----------------------------------")
            print("1 - Selecionar interface")
            print("2 - Alterar filtro")
            print("3 - Capturar pacotes (rápido)")
            print("4 - Capturar pacotes (personalizado)")
            print("5 - Mostrar últimos logs")
            print("6 - Exportar logs")
            print("7 - Sair")
            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                new_iface = choose_interface()
                if new_iface:
                    iface = new_iface
                    print(f"[OK] Interface definida: {iface}")
                else:
                    print("[INFO] Seleção cancelada.")
                input("\nPressione ENTER para continuar...")

            elif choice == "2":
                bpf_filter = choose_filter(bpf_filter)
                input("\nPressione ENTER para continuar...")

            elif choice == "3":
                if not iface:
                    print("[ERRO] Selecione uma interface antes de capturar.")
                    input("\nPressione ENTER para continuar...")
                    continue
                print(f"[INFO] Capturando {capture_count} pacotes na interface {iface} com filtro '{bpf_filter}'...")
                analyzer.start_capture(iface=iface, count=capture_count, bpf_filter=bpf_filter)
                input("\nCaptura finalizada. Pressione ENTER para continuar...")

            elif choice == "4":
                if not iface:
                    print("[ERRO] Selecione uma interface antes de capturar.")
                    input("\nPressione ENTER para continuar...")
                    continue
                try:
                    cnt = int(input("Quantos pacotes deseja capturar? (numero): ").strip())
                except ValueError:
                    print("[ERRO] Valor inválido.")
                    input("\nPressione ENTER para continuar...")
                    continue
                print(f"[INFO] Capturando {cnt} pacotes na interface {iface} com filtro '{bpf_filter}'...")
                analyzer.start_capture(iface=iface, count=cnt, bpf_filter=bpf_filter)
                input("\nCaptura finalizada. Pressione ENTER para continuar...")

            elif choice == "5":
                show_last_captures()
                input("\nPressione ENTER para continuar...")

            elif choice == "6":
                export_logs()
                input("\nPressione ENTER para continuar...")

            elif choice == "7":
                print("Saindo... Até mais!")
                break

            else:
                print("Opção inválida. Tente novamente.")
                input("\nPressione ENTER para continuar...")

        except KeyboardInterrupt:
            print("\n[INFO] Execução interrompida pelo usuário (Ctrl+C).")
            sys.exit(0)
        except Exception as e:
            print(f"[ERRO INESPERADO] {e}")
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main_menu()
