def pair_sum(arr, sum):
    # code here
    seen = set()
    for num in arr:
        if sum - num in seen:
            return True
        seen.add(num)
    return False