import random

##### Define parameters #####
ALPHA = [chr(i) for i in range(97, 123)]
#Sentence to find
SENTENCE = "this is a test sentence"
#Genetic parameters
NB_PER_GENERATION = 1000
ELITE_PERCENTAGE = 30
MUTATION_PROB = 5


class individual:
	"""
	Individual class
	
	Attributs :
		-> size(int) : size of the genereted sentence
		-> score(int) : score of the individual according to the global const SENTENCE
	"""
	 
	def __init__(self, size):
		"""
		Constructor of Individual
		Takes one parameter size(int) which will be the length of the generated sentence
		"""
		
		self.size = size
		self.sentence = self.generate_sentence(size)
		
	def generate_sentence(self, size, alphabet):
		"""
		Takes two parameters:
			-> size(int)
			-> alphabet(char array)
		Return a string of length size with characters taken in alphabet
		"""
		sentence = ""
		while size != 0:
			sentence += ALPHA[random.randrange(0, 26)]
			size -= 1
		return sentence
		
	def compute_score(self, reference):
		"""
		Takes one parameter:
			-> reference(string)
		Return:
			-> -1 if self.sentence and reference have two different sizes
			-> else the number of corresponding characters between self.sentence and reference
		"""
		if len(reference) != size:
			return -1
		score = 0
		for i in range(size):
			score += reference[i] == self.sentence[i]
		return score
					
a = individual(10)
print(a.sentence)
		
