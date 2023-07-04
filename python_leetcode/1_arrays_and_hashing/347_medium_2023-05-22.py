def topKFrequent(nums, k):
    freq = {}
    for num in nums:
        freq[str(num)] = 1 + freq.get(str(num), 0)
    itms = [(key, value) for key, value in freq.items()]
    result = sorted(itms, key=lambda itms: itms[1], reverse=True)
    return [int(x[0]) for x in result][:k]
