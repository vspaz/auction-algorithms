from typing import List, Union


class SimpleAuction:

    @staticmethod
    def get_first_price_auction_utility(bidder_valuation: Union[int, float],
                                        bidder_bid: Union[int, float],
                                        winning_bid: Union[int, float]) -> int:
        if bidder_bid == winning_bid:
            return bidder_valuation - bidder_bid
        return 0

    @staticmethod
    def get_second_price_auction_utility(bidder_valuation: Union[int, float],
                                         second_highest_bid: Union[int, float],
                                         winning_bid: Union[int, float]) -> int:
        if bidder_valuation == winning_bid:
            return bidder_valuation - second_highest_bid
        return 0

    @staticmethod
    def get_winning_bid_and_second_highest_bid(bids: List[Union[int, float]]):
        bids_sorted_desc = sorted(bids, reverse=True)
        winning_bid = bids_sorted_desc[0]
        second_highest_bid = bids_sorted_desc[1]
        return winning_bid, second_highest_bid

    @staticmethod
    def is_auction_individually_rational(utilities: List[Union[int, float]]) -> bool:
        return all(u >= 0 for u in utilities)

    @staticmethod
    def is_auction_incentive_compatible(bids: List[Union[int, float]], valuations: List[Union[int, float]]) -> bool:
        return bids == valuations
