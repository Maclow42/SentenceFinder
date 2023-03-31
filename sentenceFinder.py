import random

##### Define parameters #####
ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.;:/!?\n"
ALPHA_LENGTH = len(ALPHA)
#Genetic parameters
GENERATION_SIZE = 2000
ELITE_PERCENTAGE = 20
MUTATION_PROB = 0.01
#Sentence to find
SENTENCE = "The world is a vast and fascinating place, full of wonder and mystery."

class Individual:
	"""
	Individual class
	
	Attributs :
		-> size(int) : size of the genereted sentence
		-> sentence(string) : sentence of Individual
	"""
	 
	def __init__(self, size):
		"""
		Constructor of Individual
		Takes one parameter:
			-> size(int) which will be the length of the generated sentence
			-> initialise self.sentence as ""
		"""
		
		self.size = size
		self.sentence = ""
		
	def generate_sentence(self):
		"""
		Takes one parameters:
			-> size(int)
		Return a string of length size with characters taken in const ALPHA
		"""
		random.seed()
		sentence = ""
		size = self.size
		while size != 0:
			sentence += ALPHA[random.randint(0, ALPHA_LENGTH-1)]
			size -= 1
		self.sentence = sentence
		return
		
	def compute_fitness(self):
		"""
		Return:
			-> the number of corresponding characters between self.sentence and SENTENCE
		"""
		score = 0
		for i in range(self.size):
			score += SENTENCE[i] == self.sentence[i]
		return score
		
def get_child(ind1, ind2):
	"""
	Takes 3 parameters:
		-> ind1 (Individual)
		-> ind2 (Individual)
	return an Individual based on genetics of ind1 and ind2 with a mutation probability of MUTATION_PROB
	return None if MUTATION_PROB is not a percentage or if ind1 and ind2 have two different sizes
	"""
	#If mutation_prof is not a probability
	if MUTATION_PROB < 0 or MUTATION_PROB > 1:
		printf("ERROR : MUTATION_PROB is not a probability (not included in [0, 1]")
		return None
	if ind1.size != ind2.size:
		printf("ERROR : ind1 and ind2 have two different sizes")
		return None
		
	random.seed()
	child = Individual(ind1.size)
	for i in range(child.size):
		p = random.random()
		if p < MUTATION_PROB :
			child.sentence += ALPHA[random.randint(0, ALPHA_LENGTH-1)]
		elif p < (1-MUTATION_PROB)/2:
			child.sentence += ind1.sentence[i]
		else:
			child.sentence += ind2.sentence[i]
	return child
	
def create_generation(size, sizeind, parents=None):
	"""
	Takes 3 arguments:
		-> size(int) : number of Individual in generation
		-> sizeind(int) : size of Individuals
		-> parents(Individual array) : if not None, parents used to create generation
	Return an Individual array of length size
	"""
	random.seed()
	generation = []
	#if parents are specified
	if parents:
		nbp = len(parents)
		#place again parents
		for p in parents:
			generation.append(p)
		#create random children
		for i in range(nbp, size):
			p1 = parents[random.randint(0, nbp-1)]
			p2 = parents[random.randint(0, nbp-1)]
			generation.append(get_child(p1, p2))
	else:
		for i in range(size):
			ind = Individual(sizeind)
			ind.generate_sentence()
			generation.append(ind)
	return generation
	
def get_elite(generation):
	"""
	Takes one argument:
		-> generation(Individual array)
	Returns:
		-> the ELITE_PERCENTAGE% best individuals in generation
		-> None if ELITE_PERCENTAGE is not a percentage
	"""
	
	if ELITE_PERCENTAGE < 0 or ELITE_PERCENTAGE > 100:
		print("ERROR : ELITE_PERCENTAGE is not a percentage (not included in [0, 100]")
		return None
		
	#sort generation in decreasing order according to element's fitness
	generation = sorted(generation, key=lambda x : -x.compute_fitness())
	nbToTake = ELITE_PERCENTAGE * len(generation) //100
	elite = []
	for i in range(nbToTake):
		elite.append(generation[i])
		
	return elite
		
		
def main():
	i = 0
	L = len(SENTENCE)
	generation = create_generation(GENERATION_SIZE, L)
	elite = get_elite(generation)
	print("Generation n°" + str(i))
	print(elite[0].sentence, "-> score:", str(elite[0].compute_fitness()) + "/" + str(L), "\n")
	
	
	while(elite[0].compute_fitness() != L):
		i += 1
		generation = create_generation(GENERATION_SIZE, L, elite)
		elite = get_elite(generation)
		print("Generation n°" + str(i))
		#print the best of all generation
		print(elite[0].sentence, "-> score:", str(elite[0].compute_fitness()) + "/" + str(L), "\n")

if __name__ == "__main__":
   main()
