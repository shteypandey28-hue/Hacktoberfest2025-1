from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        top_k = [item for item, count in counts.most_common(k)]

        return top_k
       
