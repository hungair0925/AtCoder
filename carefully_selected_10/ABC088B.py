n = int(input())
cards = list(map(int, input().split()))

alice = []
bob = []

while len(cards) > 0:
    alice_card = max(cards)
    alice.append(alice_card)
    cards.remove(alice_card)
    
    if len(cards) == 0:
        break
    bob_card = max(cards)
    bob.append(bob_card)
    cards.remove(bob_card)


print(sum(alice) - sum(bob))