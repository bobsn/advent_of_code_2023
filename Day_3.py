import advent_functions as af


class Day_3():
    def __init__(self):
        self.text = af.get_text(3) # 140x140
        self.max_idx = len(self.text[0])-1
            
    def part_1(self):
        sum_part_numbers = 0
        current_number = ''
        for y_idx, line in enumerate(self.text):
            for x_idx, value in enumerate(line):
                if value.isnumeric():
                    current_number += value
                # Number exists and no new number is added
                elif current_number:
                    number_length = len(current_number)
                    applicable_indices = self.determine_applicable_indices(y_idx=y_idx, x_idx=x_idx, x_len=number_length)
                    part_number = self.find_symbol(applicable_indices)
                    if part_number:
                        sum_part_numbers += int(current_number)
                    current_number = ''
                    continue

                # Last possible number -> Do not like copy-pasting, but it works for now
                if current_number and x_idx == self.max_idx:
                    number_length = len(current_number)
                    applicable_indices = self.determine_applicable_indices(y_idx=y_idx, x_idx=x_idx, x_len=number_length)
                    part_number = self.find_symbol(applicable_indices)
                    if part_number:
                        sum_part_numbers += int(current_number)
                    current_number = ''
        
        print("The final sum of the part numbers is: ", sum_part_numbers)


    def determine_applicable_indices(self, y_idx, x_idx, x_len):
        y_indices = [y for y in [y_idx-1, y_idx, y_idx+1] if y >= 0 and y < self.max_idx]
        x_indices = [x for x in range(x_idx-x_len-1, x_idx+1) if x >= 0 and x < self.max_idx]
        # Applicable indices also looks at the numbers that it is checking around. Removing those numbers from this
        # feels like a waste of time, given that removing those numbers also requires computation time.
        applicable_indices = {y:x_indices for y in y_indices}
        return applicable_indices
    

    def find_symbol(self, indices):
        value_list = [self.text[key][value] for key, values in indices.items() for value in values]
        value_list = [value for value in value_list if not value.isnumeric() and value != '.']        
        return value_list
    

    def find_part_numbers(self, indices):
        parts_amount = 0
        part_indices = []
        for key, values in indices.items():
            same_number = False
            for value in values:
                if self.text[key][value].isnumeric() and same_number == False:
                    parts_amount += 1
                    same_number = True
                    part_indices.append([key,value])
        if parts_amount == 2:
            return part_indices
        else:
            return False
    

    def find_full_numbers(self, part_indices):
        gear_ratios = None
        # TODO: NYI
        return gear_ratios

    def part_2(self):
        sum_gear_ratio = 0
        current_number = ''
        for y_idx, line in enumerate(self.text[:5]):
            star_indices = [idx for idx, v in enumerate(line) if v == '*']
        
            for idx in star_indices:
                applicable_indices = self.determine_applicable_indices(y_idx=y_idx, x_idx=idx, x_len=1)
                part_indices = self.find_part_numbers(applicable_indices)
                if part_indices:
                    gear_ratios = self.find_full_numbers(part_indices)
                    sum_gear_ratio += int(gear_ratios[0])*int(gear_ratios[1])
                current_number = ''
                continue

                # Last possible number -> Do not like copy-pasting, but it works for now
                if current_number and x_idx == self.max_idx:
                    number_length = len(current_number)
                    applicable_indices = self.determine_applicable_indices(y_idx=y_idx, x_idx=x_idx, x_len=number_length)
                    part_number = self.find_symbol(applicable_indices)
                    if part_number:
                        sum_part_numbers += int(current_number)
                    current_number = ''
        
        print("The final sum of the gear ratio is: ", sum_gear_ratio)


if __name__ == "__main__":
    day3 = Day_3()
    day3.part_1()
    day3.part_2()