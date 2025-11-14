# Analisador de Pacotes Ethernet

Projeto desenvolvido para a disciplina **Projetos de Infraestrutura de Comunicação**, com o objetivo de capturar, analisar e registrar pacotes Ethernet reais utilizando Python e Scapy. O sistema permite visualizar informações da camada de enlace e entender a estrutura básica de quadros Ethernet na prática.

---

## Equipe
- Janderson Ferreira  
- Pedro  
- Hyngrid  
- Maria Aparecida  
- Diego  
- Pamela  

---

## Descrição do Projeto
O projeto implementa:

### ✓ Captura de Pacotes (Scapy)
- Seleção da interface de rede
- Aplicação de filtros BPF (ether, arp, ip, ip6…)
- Exibição em tempo real dos dados:
  - MAC de origem  
  - MAC de destino  
  - EtherType  
- Armazenamento automático dos pacotes em um arquivo JSON (`logs/packets.json`)

### ✓ Interface em Menu (CLI)
Menu funcional com opções:
- Selecionar interface  
- Modificar filtro  
- Capturar pacotes (rápido ou personalizado)  
- Exibir últimos logs  
- Exportar registros  
- Sair  

### ✓ Estrutura Modular
Organização do código em módulos:
- `analyzer.py` – captura/análise com Scapy  
- `packet.py` – classe do modelo de pacote  
- `utils.py` – manipulação de logs e utilidades  
- `interface.py` – menu do sistema  
- `main.py` – ponto de entrada  

### ✓ Testes Unitários
- Teste da classe `Packet` verificando:
  - Inicialização correta  
  - Representação textual  

---

## Requisitos
- Python 3.10+
- Scapy instalado: pip install scapy

--- 

## Como Executar
1. Abrir o terminal na pasta do projeto  
2. Rodar o arquivo principal: python main.py
3. Navegar pelo menu interativo.

---

## Status do Projeto
✔ Código finalizado  
✔ Testes implementados  
✔ Log funcional  
✔ Documentação concluída  
✔ Pronto para apresentação
