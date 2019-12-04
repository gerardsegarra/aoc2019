init = 145852
limit = 616942
total = 0

def proccess(init): 
    has_adjacents = False
    almost_has_adjacents = False
    is_incr = True
    prev = -1
    num_list = {}
    for num in str(init):
        num = int(num)
        if num < prev:
            is_incr = False
            break
        
        if prev == num:
            num_list[num] = num_list.get(num, 1) + 1 
    
        prev = num
    
    for item in num_list:
        if num_list[item] == 2:
            has_adjacents = True
    return has_adjacents and is_incr


while init < limit:

    if proccess(init):
        total = total + 1
    init = init + 1


print("total", total)
