


if __name__ == "__main__":
    # open input file, read lines
    f = open("input.txt")
    lines = f.readlines()

    # hold result
    res = 0
    
    for line in lines:
        curr = 0
        
        _, nums = line.split(":")       # split off game info
        keys, nums = nums.split("|")    # split off keys and nums
        
        arr = []
        for k in keys.split():
            arr.append(int(k))
        
        for n in nums.split():
            if int(n) in arr:
                if curr == 0:
                    curr = 1
                else:
                    curr *= 2
        
        res += curr
        
    print(res)