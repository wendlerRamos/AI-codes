
def check_if_user_type_only_digits(chromossomeSize, populationSize, crossingProbability, mutationProbability,
                              methodOfSelection, elitismSize, quantityOfCrossing, quantityOfGeneration):
    if not chromossomeSize.isdigit(): return False
    if not populationSize.isdigit(): return False
    if not crossingProbability.isdigit(): return False
    if not mutationProbability.isdigit(): return False
    if not methodOfSelection.isdigit(): return False
    if not elitismSize.isdigit(): return False
    if not quantityOfCrossing.isdigit(): return False
    if not quantityOfGeneration.isdigit(): return False
    return True

def format_binary_code(binaryCode):
    #getting only the binari part of 0b0101010
    binaryString = str(binaryCode).split("b")[1]
    for i in range(8-len(binaryString)):
        binaryString = "0" + binaryString
    return binaryString

def calculate_fitness(value_x, value_y):
    import math
    result = 21.5 + value_x*math.sin(4*math.pi*value_x) + value_y*math.sin(20*math.pi*value_y)
    
def calculate_roulette_probability(fitness_value, fitness_summation):
    probability = fitness_value/fitness_summation
    return probability

def make_crossover(genetic_algoritm):

    pass

def make_mutation(cromossome):
    
    pass