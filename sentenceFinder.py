import random

##### Define parameters #####
ALPHA = [chr(i) for i in range(32, 123)]
ALPHA_LENGTH = len(ALPHA)
#Sentence to find
SENTENCE = "this is a test sentence"
#Genetic parameters
NB_PER_GENERATION = 1000
ELITE_PERCENTAGE = 30
MUTATION_PROB = 0.05


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
		
	def compute_score(self, reference):
		"""
		Takes one parameter:
			-> reference(string)
		Return:
			-> -1 if self.sentence and reference have two different sizes
			-> else the number of corresponding characters between self.sentence and reference
		"""
		if len(reference) != self.size:
			return -1
		score = 0
		for i in range(self.size):
			score += reference[i] == self.sentence[i]
		return score
		
def get_child(ind1, ind2, mutation_prob):
	"""
	Takes 3 parameters:
		-> ind1 (Individual)
		-> ind2 (Individual)
		-> mutation_prob(int, percentage)
	return an Individual based on genetics of ind1 and ind2 with a mutation probability of mutation_prob
	return None if an error occured
	"""
	#If mutation_prof is not a probability
	if mutation_prob < 0 or mutation_prob > 1:
		return None
	if ind1.size != ind2.size:
		return None
		
	random.seed()
	child = Individual(ind1.size)
	for i in range(child.size):
		p = random.random()
		if p < mutation_prob :
			child.sentence += ALPHA[random.randint(0, ALPHA_LENGTH-1)]
		elif p < (1-mutation_prob)/2:
			child.sentence += ind1.sentence[i]
		else:
			child.sentence += ind2.sentence[i]
	return child
	
def create_generation(size, sizeind, parents=None):
	"""
	Takes 3 arguments:
		-> size(int) : number of Individual in generation
		->sizeind(int) : size of Individuals
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
			generation.append(get_child(p1, p2, MUTATION_PROB))
	else:
		for i in range(size):
			ind = Individual(sizeind)
			ind.generate_sentence()
			generation.append(ind)
	return generation
		
		
		
a = create_generation(3, 5)
for e in a:
	print(e.sentence)
