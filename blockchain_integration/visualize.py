import matplotlib.pyplot as plt

def plot_consensus(votes_dict):
    nodes = list(votes_dict.keys())
    votes = list(votes_dict.values())

    plt.figure(figsize=(8,5))
    plt.bar(nodes, votes)
    plt.title("Consensus Votes per Node")
    plt.xlabel("Nodes")
    plt.ylabel("Votes")
    plt.tight_layout()
    plt.show(block=True)