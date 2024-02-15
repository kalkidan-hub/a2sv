class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coin_map = {5:0,10:0}
        for coin in bills:
            print(coin_map)
            if coin == 5:
                coin_map[5] += 1
            elif coin == 10:
                coin_map[10] += 1
                coin_map[5] -= 1
                if coin_map[5] < 0:
                    return False
            else:
                coin_map[5] -= 1
                if coin_map[10]:
                    coin_map[10] -= 1
                else:
                    coin_map[5] -= 2
                if coin_map[5] < 0 or coin_map[10] < 0:
                    return False

                
        return True

        return 
        