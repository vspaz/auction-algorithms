from auctions.simple_auction import SimpleAuction


def test_get_first_price_auction_utility_ok():
    bidder_utility = SimpleAuction.get_first_price_auction_utility(bidder_valuation=110, bid=100, winning_bid=100)
    assert bidder_utility == 10

def test_get_second_price_auction_utility_ok():
    bidder_utility = SimpleAuction.get_second_price_auction_utility(bidder_valuation=110, second_highest_bid=90, winning_bid=100)
    assert bidder_utility == 0

def test_get_winning_bid_and_second_highest_bid_ok():
    bid, second_highest_bid = SimpleAuction.get_winning_bid_and_second_highest_bid(bids=[110, 80, 90])
    assert bid == 110
    assert second_highest_bid == 90

def test_is_auction_individually_rational_ok():
    assert SimpleAuction.is_auction_individually_rational(utilities=[10, 5, 20, 50, 30]) is True

def test_is_auction_individually_rational_fail():
    assert SimpleAuction.is_auction_individually_rational(utilities=[10, 5, -5, 50, 30]) is False

def test_is_auction_incentive_compatible():
    assert SimpleAuction.is_auction_incentive_compatible(bids=[1, 2, 4, 5], valuations=[1, 2, 4, 5]) is True
