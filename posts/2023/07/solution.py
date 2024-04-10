import collections


with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def primary_order(hand):
    counts = [count for card, count in collections.Counter(hand).most_common()]

    possible_counts = [
        [1, 1, 1, 1, 1],  # High card
        [2, 1, 1, 1],  # One pair
        [2, 2, 1],  # Two pair
        [3, 1, 1],  # Three of a kind
        [3, 2],  # Full house
        [4, 1],  # Four of a kind
        [5],  # Five of a kind
    ]

    return possible_counts.index(counts)


def secondary_order(hand):
    return tuple("23456789TJQKA".index(card) for card in hand)


def hand_bid_order(hand_bid):
    hand, bid = hand_bid
    return primary_order(hand), secondary_order(hand)


hands_bids = [line.split(" ") for line in lines]
hands_bids.sort(key=hand_bid_order)
answer1 = sum(i * int(bid) for i, (_, bid) in enumerate(hands_bids, 1))
print(answer1)


# Part 2
def hand_bid_order_wild(hand_bid):
    hand, bid = hand_bid
    return (
        max(primary_order(hand.replace("J", c)) for c in "23456789TQKA"),
        secondary_order(hand),
    )


hands_bids.sort(key=hand_bid_order_wild)
answer2 = sum(i * int(bid) for i, (_, bid) in enumerate(hands_bids, 1))
print(answer2)
