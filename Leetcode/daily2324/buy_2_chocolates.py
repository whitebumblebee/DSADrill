#  Link : https://leetcode.com/problems/buy-two-chocolates/description/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        new_money = money - (prices[0] + prices[1])
        if new_money >= 0:
            return new_money
        return money