init = 145852
total = 0

def proccess(init): 
    has_adjacents = False
    is_incr = True
    prev = 0
    for num in str(init):
        num = int(num)
        if num == prev:
            has_adjacents = True

        if num < prev:
            is_incr = False
            break

        prev = num
    return has_adjacents and is_incr


while init < 616942:
    #print(init)

    if proccess(init):
        total = total + 1
    init = init + 1


print("total", total)
