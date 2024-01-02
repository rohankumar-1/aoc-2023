

if __name__ == "__main__":
    # open input file, read lines
    f = open("input.txt")
    lines = f.readlines()

    # hold result
    res = []
    
    # this chunk creates list of all match #s for each value
    for line in lines:
        curr = 0
        
        _, nums = line.split(":")       # split off game info
        keys, nums = nums.split("|")    # split off keys and nums
        
        arr = []
        for k in keys.split():
            arr.append(int(k))
        
        for n in nums.split():
            if int(n) in arr:
                curr += 1
        
        res.append(curr)
    
    # create number of cards
    cards = [1] * len(res)
    
    # extend values
    for i in range(len(res)):
        # break if we have no more cards
        if cards[i] == 0:
            print(sum(cards))
            break
        
        for j in range(res[i]):
            cards[i+j+1] += cards[i]
    
    print(res)
    print(cards)
    print(sum(cards))