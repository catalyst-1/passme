def lfsr(v):
    state = (1<<127)|1
    res ="0b"
    for i in range(v+1):
        new_b = (state)&1
        res += newb
        state = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7))
    return int(res,2)
