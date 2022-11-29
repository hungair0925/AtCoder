n = int(input())
cards = list(map(int, input().split()))

sorted_cards = sorted(cards)
sorted_cards_by_player = []

for i, card in enumerate(sorted_cards):
    if n % 2 == 1:
        if i % 2 == 0:
            sorted_cards_by_player.append(card)
        else:
            sorted_cards_by_player.append(card * -1)
    else:
        if i % 2 == 1:
            sorted_cards_by_player.append(card)
        else:
            sorted_cards_by_player.append(card * -1)

print(sum(sorted_cards_by_player))