from collections import Counter

def reach_consensus(transactions):
    count = Counter(transactions)
    agreed_txn, votes = count.most_common(1)[0]
    return agreed_txn, votes