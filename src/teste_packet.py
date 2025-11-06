# test_packet.py

import unittest
from packet import Packet 
class TestPacket(unittest.TestCase):
    """
    Testes unitários para a classe Packet em packet.py.
    """

    def test_packet_initialization(self):
        """Testa se a classe Packet é inicializada corretamente com os dados."""
        # Configuração (Setup)
        src = "00:11:22:33:44:55"
        dst = "AA:BB:CC:DD:EE:FF"
        p_type = "0x0806" 

        packet = Packet(source_mac=src, destination_mac=dst, eth_type=p_type)
        self.assertEqual(packet.source_mac, src, "O MAC de origem não foi salvo corretamente.")
        self.assertEqual(packet.destination_mac, dst, "O MAC de destino não foi salvo corretamente.")
        self.assertEqual(packet.eth_type, p_type, "O Tipo Ethernet não foi salvo corretamente.")

    def test_packet_string_representation(self):
        """Testa se o método __str__ (a representação do texto) está formatado corretamente."""
        
        # Configuração
        src = "C0:FF:EE:C0:FF:EE"
        dst = "DE:AD:BE:EF:DE:AD"
        p_type = "0x0800" 
        packet = Packet(source_mac=src, destination_mac=dst, eth_type=p_type)
        
        # Valor Esperado
        expected_str = f"Pacote Ethernet: {src} -> {dst} | Tipo: {p_type}"
        self.assertEqual(str(packet), expected_str, "A string de representação do pacote está incorreta.")

if __name__ == '__main__':
    unittest.main()