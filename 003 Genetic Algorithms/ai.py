# Create target string, starting from random string
# using Genetic Algorithm

import random

POPULATION_SIZE = 100

# Valid genes
GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '''

# Target string to be generated
TARGET = "Im pretty much into AI"

class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self):
        global GENES
        gene =random.choice(GENES)
        return gene


    @classmethod
    def create_gnome(self):
        global TARGET
        gnome_len = len(TARGET)
        return [self.mutated_genes() for _ in range(gnome_len)]

    def mate(self, par2):
        child_chromosome = []

        for p1, p2 in zip(self.chromosome, par2.chromosome):

            prob = random.random()

            if prob<0.45:
                child_chromosome.append(p1)
            elif prob<0.90:
                child_chromosome.append(p2)
            else:
                child_chromosome.append(self.mutated_genes())

        return Individual(child_chromosome)


    def cal_fitness(self):
        global TARGET

        fitness =0
        for s,t in zip(self.chromosome, TARGET):
            if s!= t:
                fitness+=1
        return fitness


def main():
    global POPULATION_SIZE
    generation = 1

    population = [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

    while True:

        population = sorted(population, key=lambda x: x.fitness)

        if population[0].fitness <= 0:
            break

        new_geration = []

        s =int((10*POPULATION_SIZE)/100)

        new_geration.extend(population[0:s])

        s= int((90*POPULATION_SIZE)/100)

        for _ in range(s):
            parent1 = random.choice(population[0:50])
            parent2= random.choice(population[0:50])

            child = parent1.mate(parent2)
            new_geration.append(child)


        population = new_geration

        print ( "Generation {}\t\tString {}\t\tFitness : {}". \
                format(generation,
                       "".join(population[0].chromosome),
                    population[0].fitness))

        generation += 1

    print("Generation {}\t\tString {}\t\tFitness : {}". \
          format(generation,
                 "".join(population[0].chromosome),
                 population[0].fitness))


if __name__ == '__main__':
    main()