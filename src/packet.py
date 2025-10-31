class Packet:
    def __init__(self, source_mac, destination_mac, eth_type):
        self.source_mac = source_mac
        self.destination_mac = destination_mac
        self.eth_type = eth_type

    def __str__(self):
        return f"Pacote Ethernet: {self.source_mac} -> {self.destination_mac} | Tipo: {self.eth_type}"
