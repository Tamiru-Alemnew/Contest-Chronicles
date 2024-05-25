def distribute_cards(n, cards):
    indexed_cards = [(cards[i], i + 1) for i in range(n)]
    
    indexed_cards.sort()
    
    pairs = []
    for i in range(n // 2):
        first_card = indexed_cards[i]
        second_card = indexed_cards[n - i - 1]
        pairs.append((first_card[1], second_card[1]))

    for pair in pairs:
        print(pair[0], pair[1])

n = int(input())
cards = list(map(int, input().split()))
distribute_cards(n, cards)
