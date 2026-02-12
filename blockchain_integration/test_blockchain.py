from blockchain import Blockchain
from node import Node
from consensus import reach_consensus
from collections import Counter
from visualize import plot_consensus

# Create blockchain
bc = Blockchain()

# Create nodes
nodes = [Node(i) for i in range(5)]

# Each node proposes transaction
transactions = [node.propose_transaction() for node in nodes]

print("Proposed Transactions:")
for t in transactions:
    print(t)

# Consensus
agreed_txn, votes = reach_consensus(transactions)

print("\nAgreed Transaction:", agreed_txn)

# Add block
bc.add_block([agreed_txn])

print("\nBlockchain Length:", len(bc.chain))

# Visualization
vote_counts = Counter(transactions)
plot_consensus(vote_counts)