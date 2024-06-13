import advent_functions as af

#################################
# Part 1
#################################

text = af.open_current_file(current_day=1)

def find_digit_in_string(line:str, reversed:bool=False)->str:
    direction = -1 if reversed else 1
    for character in line[::direction]:
        if character.isdigit():
            return character

def part_1():
    sum = 0
    for textline in af.get_lines(1):
        first_number = find_digit_in_string(textline)
        last_number = find_digit_in_string(textline, reversed=True)
        
        combined_number = first_number + last_number
        sum += int(combined_number)   

    print("The total sum is: ", sum)

#########################
# Simpel maar inefficiënt

# sum = 0
# for textline in text:
#     numbers = [t for t in textline if t.isdigit()]
#     combined_number = numbers[0] + numbers[-1]
    
#     sum += int(combined_number)



#################################
# Part 2
#################################
  

def find_digit_in_string_2(line:str, reversed:bool=False)->str:
    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4', 
        'five': '5',
        'six':  '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    direction = -1 if reversed else 1
    
    for index in range(len(line))[::direction]:
        if line[index].isdigit():
            return line[index]
        else:
            for key, value in number_dict.items():
                if index+len(key) <= len(line):
                    if line[index:index+len(key)]== key:
                        return value

def part_2():
    sum = 0
    # test_list = ['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']
    # for textline in test_list:
    for textline in af.get_lines(1):
        first_number = find_digit_in_string_2(textline)
        last_number = find_digit_in_string_2(textline, reversed=True)
        
        combined_number = first_number + last_number
        sum += int(combined_number)   
        print(f"\ntextline: {textline}\ncombined_number: {combined_number}\nsum: {sum}")

    print("The total sum is: ", sum)

part_2()