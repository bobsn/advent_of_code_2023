import advent_functions as af
import numpy as np

class Day_2():
    def __init__(self):
        self.text = af.get_lines(current_day=2)

        self.bag_colours = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        self.bag_min_size= min(self.bag_colours.values())
    
    
    def part_1(self):
        final_score = 0

        # Potential caveat: If a specific color is picked twice in one sitting
        for line in self.text:
            success = True
            game_nr, round_variables = self.game_prep(line)            

            for idx, nr in enumerate(round_variables[::2]):
                nr = int(nr)
                if nr > self.bag_min_size:
                    colour = round_variables[idx*2 + 1]
                    if self.bag_colours[colour] < nr:
                        print(f"{game_nr}, with a value of {colour}: {nr}, failed.")
                        success = False
                        break
            if success:
                final_score += game_nr

        print("The final score is: ", final_score)


    def part_2(self):
        final_score = 0 #multiply rgb, sum together for that day

        for line in self.text:
            game_nr, round_variables = self.game_prep(line)
        
            round_variables_length = len(round_variables)
            minimum_cubes= {
                'red':  1,
                'green':1,
                'blue': 1
            }
            for idx in range(0, round_variables_length, 2):
                value, colour = int(round_variables[idx]), round_variables[idx+1]
                if minimum_cubes[colour] < value:
                    minimum_cubes[colour] = value
            
            cube_values = list(minimum_cubes.values())
            final_score += np.prod(cube_values)
        
        print("The final score is: ", final_score)
            


    def game_prep(self, line):
        game_nr, game = line.split(':')
        game_nr = int(game_nr.split(' ')[1])
        game_rounds = game.replace(', ', ' ').split(';')
        round_variables = [object for round in game_rounds for object in round[1:].split(" ")]
        return game_nr, round_variables


if __name__ == "__main__":
    day2 = Day_2()
    # day2.part_1()
    day2.part_2()