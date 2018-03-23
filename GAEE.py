import numpy as np
import scipy.io as sio
import numpy.linalg as la
import matplotlib.pyplot as plt
from cvxopt import solvers, matrix
from deap import base
from deap import creator
from deap import tools
import random

class GAEE(object):

	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	p = None

	npop = None
	ngen = None
	cxpb = None
	mutpb = None
	
	endmembers = None
	purepixels = None

	verbose = True

	def __init__(self, argin, verbose):
		self.verbose = verbose
		if (self.verbose):
			print ('---		Initializing GAEE algorithm')
		self.data = argin[0]
		self.nRow = argin[1]
		self.nCol = argin[2]
		self.nBand = argin[3]
		self.nPixel = argin[4]
		self.p = argin[5]

		self.npop = argin[6]
		self.ngen = argin[7]
		self.cxpb = argin[8]
		self.mutpb = argin[9]

	def princomp(self,A):
		if (self.verbose):
			print('---		Reducing data dimension (PCA)')
		M = (A-np.mean(A.T,axis=1)).T # subtract the mean (along columns)
		[latent,coeff] = la.eig(np.cov(M)) # attention:not always sorted
		score = np.dot(coeff.T,M) # projection of the data in the new space
		return coeff,score,latent

	def fitness_func(self,indice,data_pca,p):
		TestMatrix = np.zeros((p,p))
		TestMatrix[0,:] = 1
		for i in range(0,p):
			TestMatrix[1:p,i] = data_pca[:,int(indice[i])]
		volume = np.abs(la.det(TestMatrix))
		return (volume,)

	def p_attr_func(self,p,npixel):
		aux = np.random.choice(list(range(0,npixel)),p)
		return creator.Individual(aux)

	def mutation_func(self,individual,indpb,n):
		for i in range(len(individual)):
			if random.random() < indpb:
				individual[i] = type(individual[i])( np.random.randint(0,n))
		return individual

	def extract_endmember(self):
		if (self.verbose):
			print('---		Starting endmembers Extracting')
		data = self.data
		p = self.p
		k = self.npop
		ng = self.ngen
		npixel = self.nPixel
		cxpb = self.cxpb
		mutpb = self.mutpb

		creator.create("FitnessMax", base.Fitness, weights=(1.0,))
		creator.create("Individual", list, fitness=creator.FitnessMax)
		
		y = np.asarray(data)
		coeff, score, latent = self.princomp(y.T)
		data_pca = np.squeeze(score[0:p-1,:])
		toolbox = base.Toolbox()
		toolbox.register("p_attr_func", self.p_attr_func, p, npixel)
		toolbox.register("population", tools.initRepeat, list, toolbox.p_attr_func)
		toolbox.register("evaluate", self.fitness_func,data_pca=data_pca,p=p)
		toolbox.register("mate", tools.cxTwoPoint)
		toolbox.register("mutate", self.mutation_func, indpb = 0.2, n=npixel)
		toolbox.register("select", tools.selTournament, tournsize=3)
		
		random.seed(64)
		pop = toolbox.population(n=k)

		if (self.verbose):
			print("---		Starting of evolution")
		#fitnesses = list(map(toolbox.evaluate,pop))
		fitnesses = [toolbox.evaluate(ind) for ind in pop]
		for ind, fit in zip(pop, fitnesses):
			ind.fitness.values = fit
		if (self.verbose):
			print("^^^			Evaluated %i individuals" % len(pop))
		fits = [ind.fitness.values[0] for ind in pop]
		g = 0
		while g < ng:
			g = g + 1
			if (self.verbose):
				print("^^^			Generation %i" % g)
			offspring = toolbox.select(pop, len(pop))
			offspring = list(map(toolbox.clone, offspring))
			for child1, child2 in zip(offspring[::2], offspring[1::2]):
				if random.random() < cxpb:
					toolbox.mate(child1, child2)
				del child1.fitness.values
				del child2.fitness.values
			for mutant in offspring:
				if random.random() < mutpb:
					toolbox.mutate(mutant)
					del mutant.fitness.values
			fitnesses = [toolbox.evaluate(ind) for ind in offspring]
			for ind, fit in zip(offspring, fitnesses):
				ind.fitness.values = fit
			pop[:] = offspring
			# for ind in pop:
			# 	print(" %s %s " %(np.sort(ind),ind.fitness.values[0]))
			fits = [ind.fitness.values[0] for ind in pop]
			length = len(pop)
			mean = sum(fits) / length
			sum2 = sum(x*x for x in fits)
			std = abs(sum2 / length - mean**2)**0.5
			if (self.verbose):
				print("^^^			Min %s" % min(fits))
				print("^^^			Max %s" % max(fits))
				print("^^^			Avg %s" % mean)
				print("^^^			Std %s" % std)
		if (self.verbose):
			print("---		End of (successful) evolution")
		best_ind = tools.selBest(pop, 1)[0]
		if (self.verbose):
			print("---		Best individual is %s, %s" %(np.sort(best_ind) ,best_ind.fitness.values))
		S_est = data[:,best_ind]

		self.endmembers = S_est
		if (self.verbose):
			print('---		Ending endmembers Extracting')

		self.purepixels = best_ind
		return self.endmembers
