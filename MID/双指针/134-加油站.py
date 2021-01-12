"""
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

输入: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

输出: 3

解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 环长度
        mod = len(gas)

        # 起始点假设为0，当前在0节点
        start, cur = 0, 0

        # 把0节点的油灌入
        oil = gas[0]

        # 当cur + 1 == start 时说明到了终点，所以没有考虑终点到起点（两者相邻）所用的油.
        while (cur + 1) & mod != start:

            # 如果油不够下一节点
            if oil < cost[cur]:
                # 说明以start为起点不满足，前一位为起始点
                start = (start - 1) % mod
                # 更新起始点后在cur点时油量
                oil += gas[start] - cost[start]
            
            else:
                oil -= cost[cur]
                cur = (cur + 1) % mod
                oil += gas[cur]
        
        return start if oil - cost[cur] >= 0 else -1




