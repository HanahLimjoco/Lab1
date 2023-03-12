import stats

nums = [1, 2, 3, 4, 5, 6, 7, 10, 10, 20, 3]


def mode(nums):
    
    from collections import Counter

    frqs = Counter(nums)
    mc = max(frqs.values())
    modes = [num for num, count in frqs.items() if count == mc]

    if len(modes) == len(nums):
        return None
    else:
        return modes[0]

def median(nums):
    
    sn = sorted(nums)
    haba = len(nums)
    mp = haba // 2

    if haba % 2 == 0:
        return (sn[mp - 1] + sn[mp]) / 2
    else:
        return sn[mp]

def mean(nums):
    
    return sum(nums) / len(nums)


median_value = stats.median(nums)
mode_value = stats.mode(nums)
mean_value = stats.mean(nums)

print("Median:", median_value)
print("Mode:", mode_value)
print("Mean:", mean_value)