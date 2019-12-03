#input_seq = [1,12,2,3,2,3,11,0,99,30,40,50]
input_seq_final = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,1,13,23,27,1,27,6,31,2,31,6,35,2,6,35,39,1,39,5,43,1,13,43,47,1,6,47,51,2,13,51,55,1,10,55,59,1,59,5,63,1,10,63,67,1,67,5,71,1,71,10,75,1,9,75,79,2,13,79,83,1,9,83,87,2,87,13,91,1,10,91,95,1,95,9,99,1,13,99,103,2,103,13,107,1,107,10,111,2,10,111,115,1,115,9,119,2,119,6,123,1,5,123,127,1,5,127,131,1,10,131,135,1,135,6,139,1,10,139,143,1,143,6,147,2,147,13,151,1,5,151,155,1,155,5,159,1,159,2,163,1,163,9,0,99,2,14,0,0]

def process_number(number, array, position):
    if number == 1:
        subst_index = array[position + 3]
        array[subst_index] = array[array[position + 1]] + array[array[position + 2]]

    elif number == 2:
        subst_index = array[position + 3]
        array[subst_index] = array[array[position + 1]] * array[array[position + 2]]

    elif number == 99:
        return len(array)

    else:
        raise Exception("Error")

    return position + 4

def find_result(input_seq, noun, verb):

    length = len(input_seq)
    position = 0
    input_seq[1] = noun
    input_seq[2] = verb 

    while position < length:
        command = input_seq[position]
        position = process_number(command, input_seq, position)

    return input_seq[0]

noun = 0
while noun < 100:
    verb = 0
    while verb < 100:
        input_seq = input_seq_final.copy()
        try:
            #print(noun, verb)
            result = find_result(input_seq, noun, verb)
            #print(result)

            if result == 19690720:
                print("Result", noun, verb)
                break

        except Exception:
            #print("error")
            pass

        verb = verb + 1
    noun = noun + 1

