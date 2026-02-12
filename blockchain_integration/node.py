import random

class Node:
    def __init__(self, node_id):
        self.node_id = node_id

    def propose_transaction(self):
        amount = random.randint(1, 100)
        return f"Node {self.node_id} sends ${amount}"