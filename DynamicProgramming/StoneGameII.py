"""
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones.
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.
On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
"""
from functools import lru_cache

def stoneGameII(piles):
    suffix_sum = [0]

    for pile in reversed(piles):
        suffix_sum.append(suffix_sum[-1] + pile)

    suffix_sum.reverse()

    @lru_cache(None)
    def dfs(pile, M):
        sum_next_player = suffix_sum[pile]

        for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
            sum_next_player = min(
                sum_next_player, dfs(next_pile, max(M, next_pile - pile))
            )

        sum_player = suffix_sum[pile] - sum_next_player

        return sum_player

    return dfs(0, 1)

if __name__ == '__main__':
    piles = [1, 2, 3, 4, 5, 100]
    print(stoneGameII(piles))