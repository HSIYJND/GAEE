from VCA import *
from PPI import *
from NFINDR import *
from GAEE import *
from MAPS import *
import scipy.io as sio
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

class DEMO(object):

	name = None

	ee = None
	am = None
	
	data = None
	nRow = None
	nCol = None
	nBand = None
	nPixel = None
	selectedBands = None
	p = None 

	thr = None

	groundtruth = None
	num_gtendm = None

	raw_endmembers = None
	abundances = None

	sam_endmembers = None
	sam_values = None
	sam_mean = None
	sam_std = None

	sid_endmembers = None
	sid_values = None
	sid_mean = None
	sid_std = None

	verbose = True

	def __init__(self, argin,verbose):
		if (verbose):
			print('... Initializing DEMO')
		self.verbose = verbose
		self.load_data(argin[0])
		self.load_groundtruth(argin[1])
		self.data = self.convert_2D(self.data)
		
		self.p = argin[2]
		self.name = argin[3]
		
		if argin[3] == 'VCA':
			if (verbose):
				print('... Selecting VCA endmember extractor')
			self.ee = VCA([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p],self.verbose)
		if argin[3] == 'PPI':
			nSkewers = argin[4]
			initSkewers = argin[5]
			if (verbose):
				print('... Selecting PPI endmember extractor')
			self.ee = PPI([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, nSkewers, initSkewers],self.verbose)
		if argin[3] == 'NFINDR':
			maxit = argin[4]
			if (verbose):
				print('... Selecting NFINDR endmember extractor')
			self.ee = NFINDR([self.data.T,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, maxit],self.verbose)
		if argin[3] == 'ATGP':
			if (verbose):
				print('... Selecting ATGP endmember extractor')
			self.ee = ATGP([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p],self.verbose)		
		if argin[3] == 'FIPPI':
			maxit = argin[4]
			if (verbose):
				print('... Selecting FIPPI endmember extractor')
			self.ee = FIPPI([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, maxit],self.verbose)	
		if argin[3] == 'GAEE' or argin[3] == 'GAEE-IVFm' or argin[3] == 'GAEE-VCA' or argin[3] == 'GAEE-IVFm-VCA':
			npop = argin[4]
			ngen = argin[5]
			cxpb = argin[6]
			mutpb = argin[7]
			initPurePixels = argin[8]
			ivfm = argin[9]
			if (verbose):
				print('... Selecting GAEE endmember extractor')
			self.ee = GAEE([self.name,self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, npop,
				ngen,cxpb,mutpb,initPurePixels,ivfm],self.verbose)		

		if (verbose):
			print('... Selecting NNLS abundance mapper')
		self.am = UCLS([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p],verbose)

	def extract_endmember(self):
		if (verbose):
			print('... Extracting endmembers')
		self.raw_endmembers = self.ee.extract_endmember()[0]

	def map_abundance(self):
		if (verbose):
			print('... Mapping abundances')
		self.am.endmembers = self.raw_endmembers
		self.abundances = self.am.map_abundance()

	def load_data(self,data_loc):
		if (verbose):
			print('... Loading data')

		pkg_data = sio.loadmat(data_loc)
		self.data = pkg_data['X']
		
		self.nRow = self.data.shape[0]
		self.nCol = self.data.shape[1]
		self.nBand = self.data.shape[2]
		self.selectedBands = pkg_data['BANDS'][0]

	def load_groundtruth(self,gt_loc):
		if (verbose):
			print('... Loading groundtruth')
		pkg_gt = sio.loadmat(gt_loc)
		self.groundtruth = pkg_gt['Y']
		self.num_gtendm = self.groundtruth.shape[1]

	def convert_2D(self,data):
		if (verbose):
			print('... Converting 3D data to 2D')
		self.nPixel = self.nRow*self.nCol
		data_2D = np.asmatrix(data.reshape((self.nRow*self.nCol,self.nBand))).T
		return data_2D

	def convert_3D(self,data):
		if (verbose):
			print('... Converting 2D data to 3D')
		data_3D = np.asarray(data)
		data_3D = data_3D.reshape((self.nRow,self.nCol,self.p))
		return data_3D

	def print_purepixels(self):
		if (verbose):
			print('... Printing pure pixels')
		print(self.ee.purepixels)

	def plot_abundance(self,i):
		if (verbose):	
			print('... Plotting abundance')
		plt.matshow(self.abundances[:,:,i])

	def plot_groundtruth(self,i):
		if (verbose):
			print('... Plotting groundtruth')
		plt.plot(self.groundtruth[:,i])
		plt.title(str(i))
		plt.xlabel('wavelength (µm)')
		plt.ylabel('reflectance (%)')
		plt.tight_layout()

	def plot_groundtruth_ab(self):
		if (verbose):
			print('... Plotting groundtruth')
		plt.matshow(self.groundtruth[:,:])

	def plot_endmember(self,i):
		if (verbose):
			print('... Plotting endmember')
		plt.plot(self.raw_endmembers[:,i])
		plt.title(str(i))
		plt.xlabel('wavelength (µm)')
		plt.ylabel('reflectance (%)')
		plt.tight_layout()

	def SAM(self,a,b):
		if (verbose):
			print('... Applying SAM metric')
		[L, N] = a.shape
		errRadians = np.zeros(N)
		b = np.asmatrix(b)
		for k in range(0,N):
			tmp = np.asmatrix(a[:,k])
			s1 = tmp.T
			s2 = b
			s1_norm = la.norm(s1)
			s2_norm = la.norm(s2)
			sum_s1_s2 = s1*s2.T
			aux = sum_s1_s2 / (s1_norm * s2_norm)
			aux[aux>1.0] = 1
			angle = math.acos(aux)
			errRadians[k] = angle
		return errRadians

	def SID(self,s1,s2):
		if (verbose):
			print('... Applying SID metric')
		[L, N] = s1.shape
		errRadians = np.zeros(N)
		s1 = np.asarray(s1)
		s2 = np.asarray(s2)
		for k in range(0,N):
			tmp = s1[:,k]
			p = (tmp / np.sum(tmp)) + np.spacing(1)
			q = (s2 / np.sum(s2)) + np.spacing(1)
			angle = np.sum(p.T * np.log(p / q) + q * np.log(q / p))

			if np.isnan(angle):
				errRadians[k] = 0
			else:
				errRadians[k] = angle

		return errRadians

	def best_sam_match(self): # Best Estimated endmember for the groundtruth
		if (verbose):
				print('... Matching best endmember and groundtruth pair')
		sam = np.zeros((self.num_gtendm,self.p))
		sid = np.zeros((self.num_gtendm,self.p))

		for i in range(self.raw_endmembers.shape[1]):
			sam[i,:] = self.SAM(self.raw_endmembers,self.groundtruth[self.selectedBands,:][:,i])
			sid[i,:] = self.SID(self.raw_endmembers,self.groundtruth[self.selectedBands,:][:,i])

		idxs = [list(x) for x in np.argsort(sam,axis=1)]
		values = [list(x) for x in np.sort(sam,axis=1)]
		pidxs = list(range(self.p))
		aux = []

		for i in range(self.num_gtendm):
			for j in range(self.p):
				aux.append([pidxs[i],idxs[i][j],values[i][j]])

		aux = sorted(aux, key=lambda x: x[2])
		new_idx = [0]*self.p
		new_value = [0]*self.p

		for i in range(self.p):
			a_idx, b_idx, c_value = aux[0]
			new_idx[a_idx] = b_idx
			new_value[a_idx] = c_value
			aux = [x for x in aux if x[0] != a_idx and x[1] != b_idx]

		self.sam_endmembers = self.raw_endmembers[:,new_idx]

		return [new_idx, new_value]

	def best_sid_match(self): # Best Estimated endmember for the groundtruth
		if (verbose):
				print('... Matching best endmember and groundtruth pair')
		sid = np.zeros((self.num_gtendm,self.p))
		for i in range(self.raw_endmembers.shape[1]):
			sid[i,:] = self.SID(self.raw_endmembers,self.groundtruth[self.selectedBands,:][:,i])
	
		idxs = [list(x) for x in np.argsort(sid,axis=1)]
		values = [list(x) for x in np.sort(sid,axis=1)]
		pidxs = list(range(self.p))
		aux = []

		for i in range(self.num_gtendm):
			for j in range(self.p):
				aux.append([pidxs[i],idxs[i][j],values[i][j]])

		aux = sorted(aux, key=lambda x: x[2])
		new_idx = [0]*self.p
		new_value = [0]*self.p

		for i in range(self.p):
			a_idx, b_idx, c_value = aux[0]
			new_idx[a_idx] = b_idx
			new_value[a_idx] = c_value
			aux = [x for x in aux if x[0] != a_idx and x[1] != b_idx]

		self.sid_endmembers = self.raw_endmembers[:,new_idx]

		return [new_idx, new_value]

	def best_run(self,mrun): # Monte Carlo Best Estimated EM with avg SAM or SID
		if (verbose):
				print('... Starting Monte Carlo set of runs')
		sam_best_run = 9999
		sam_best_values = None
		sam_best_idx = None
		sam_best_data = None
		sam_all_runs_value = np.zeros((mrun,self.p))

		sid_best_run = 9999
		sid_best_values = None
		sid_best_idx = None
		sid_best_data = None
		sid_all_runs_value = np.zeros((mrun,self.p))

		for i in range(mrun):
			self.extract_endmember()
			[sam_idx, sam_value] = self.best_sam_match()
			[sid_idx, sid_value] = self.best_sid_match()
			
			sam_all_runs_value[i,:] = sam_value
			sid_all_runs_value[i,:] = sid_value

			if(np.mean(sam_value) < sam_best_run):
				sam_best_run = np.mean(sam_value)
				sam_best_values = sam_value
				sam_best_idx = sam_idx
				sam_best_data = self.sam_endmembers

			if(np.mean(sid_value) < sid_best_run):
				sid_best_run = np.mean(sid_value)
				sid_best_values = sid_value
				sid_best_idx = sid_idx
				sid_best_data = self.sid_endmembers

		self.sam_endmembers = sam_best_data
		self.sam_values = sam_best_values
		self.sam_mean = np.mean(sam_all_runs_value,axis=0)
		self.sam_std = np.std(sam_all_runs_value,axis=0)

		self.sid_endmembers = sid_best_data
		self.sid_values = sid_best_values
		self.sid_mean = np.mean(sid_all_runs_value,axis=0)
		self.sid_std = np.std(sid_all_runs_value,axis=0)

def best_conf(mrun,npop,ngen,cxpb,mutpb):
	if (verbose):
		print('... Searching best configuration for GAEEs algorithms')
	
	vca = DEMO([data_loc,gt_loc,num_endm,'VCA'],verbose)
	initPurePixels = vca.ee.extract_endmember()[1]

	algo_results = {'GAEE':[], 'GAEE-IVFm':[], 'GAEE-VCA':[], 'GAEE-IVFm-VCA':[]}

	for i in npop:
		for j in ngen:
			for k in cxpb:
				for l in mutpb:
					gaee = DEMO([data_loc,gt_loc,num_endm,'GAEE',i,j,k,l,None,False],verbose)
					ivfm = DEMO([data_loc,gt_loc,num_endm,'GAEE-IVFm',i,j,k,l,None,True],verbose)
					gaee_vca = DEMO([data_loc,gt_loc,num_endm,'GAEE-VCA',i,j,k,l,initPurePixels,False],verbose)
					ivfm_vca = DEMO([data_loc,gt_loc,num_endm,'GAEE-IVFm-VCA',i,j,k,l,initPurePixels,True],verbose)

					algo = [gaee, ivfm, gaee_vca, ivfm_vca]

					for m in algo:
						m.best_run(mrun)
						algo_results[m.name].append([ [i,j,k,l], np.mean(m.sam_mean) ])


	algo_bconf = {'GAEE':[], 'GAEE-IVFm':[], 'GAEE-VCA':[], 'GAEE-IVFm-VCA':[]}

	for i in algo_results:
		aux = [j[1] for j in algo_results[i]]
		indx = np.argmin(aux) 
		algo_bconf[i].append(algo_results[i][indx][0])
		
	return algo_bconf

if __name__ == '__main__':
	data_loc = "./DATA/cuprite_data.mat"
	gt_loc = "./DATA/cuprite_groundtruth.mat"

	num_endm = 12
	verbose = False
	thr = 0.8
	mrun = 100

	nSkewers = 100
	initSkewers = None

	maxit = 3*num_endm

	# npop = [10,100, 1000] # i
	# ngen = [10, 100, 1000] # j
	npop = [100] # i
	ngen = [100] # j
	cxpb = [0.5, 0.7, 1] # k
	mutpb = [0.05, 0.1, 0.3] # l

	# npop = [10] # i
	# ngen = [10] # j
	# cxpb = [0.5,1] # k
	# mutpb = [0.05] # l

	conf = best_conf(mrun,npop,ngen,cxpb,mutpb)

	gaee_conf = conf['GAEE'][0]
	ivfm_conf = conf['GAEE-IVFm'][0]
	gaee_vca_conf = conf['GAEE-VCA'][0]
	ivfm_vca_conf = conf['GAEE-IVFm-VCA'][0]

	print(gaee_conf)
	print(ivfm_conf)
	print(gaee_vca_conf)
	print(ivfm_vca_conf)

	ppi = DEMO([data_loc,gt_loc,num_endm,'PPI',nSkewers,initSkewers],verbose)
	nfindr = DEMO([data_loc,gt_loc,num_endm,'NFINDR',maxit],verbose)
	vca = DEMO([data_loc,gt_loc,num_endm,'VCA'],verbose)
	gaee = DEMO([data_loc,gt_loc,num_endm,'GAEE',gaee_conf[0],gaee_conf[1],
			gaee_conf[2],gaee_conf[3],None,False],verbose)
	ivfm = DEMO([data_loc,gt_loc,num_endm,'GAEE-IVFm',ivfm_conf[0],ivfm_conf[1],
			ivfm_conf[2],ivfm_conf[3],None,True],verbose)
	initPurePixels = vca.ee.extract_endmember()[1]
	gaee_vca = DEMO([data_loc,gt_loc,num_endm,'GAEE-VCA',gaee_vca_conf[0],gaee_vca_conf[1],
			gaee_vca_conf[2],gaee_vca_conf[3],initPurePixels,False],verbose)
	ivfm_vca = DEMO([data_loc,gt_loc,num_endm,'GAEE-IVFm-VCA',ivfm_vca_conf[0],ivfm_vca_conf[1],
			ivfm_vca_conf[2],ivfm_vca_conf[3],initPurePixels,True],verbose)

	endmember_names = ['Alunite','Andradite','Buddingtonite','Dumortierite','Kaolinite_1','Kaolinite_2','Muscovite',
				'Montmonrillonite','Nontronite','Pyrope','Sphene','Chalcedony','**Mean**','**Std**']
	algo = [ppi, nfindr, vca, gaee, ivfm, gaee_vca, ivfm_vca]

	tab1_sam = pd.DataFrame()
	tab1_sam['Endmembers'] = endmember_names
	tab1_sam.set_index('Endmembers',inplace=True)

	tab2_sid = pd.DataFrame()
	tab2_sid['Endmembers'] = endmember_names
	tab2_sid.set_index('Endmembers',inplace=True)

	parameters_names = ['Population Size','Number of Generations','Crossover Probability','Mutation Probability']

	tab3_conf = pd.DataFrame()
	tab3_conf['Parameters'] = parameters_names
	tab3_conf.set_index('Parameters',inplace=True)
	tab3_conf['GAEE'] = gaee_conf
	tab3_conf['GAEE-IVFm'] = ivfm_conf
	tab3_conf['GAEE-VCA'] = gaee_vca_conf
	tab3_conf['GAEE-IVFm-VCA'] = ivfm_vca_conf

	for l in algo:
		l.best_run(mrun)
		tab1_sam[l.name] = np.append(l.sam_values, [np.mean(l.sam_mean), np.mean(l.sam_std)])
		tab2_sid[l.name] = np.append(l.sid_values, [np.mean(l.sid_mean), np.mean(l.sid_std)])

	print(tab1_sam)
	print(tab2_sid)

	file = open("README.md","w")
	file.write("# Comparison of Vertex Componet Analysis (VCA) and Genetic Algorithm Endmember Extraction (GAEE) algorithms for Endmember Extraction"+"\n\n")
	file.write("## Douglas Winston R. S., Gustavo T. Laureano, Celso G. Camilo Jr.\n\n")
	file.write("Endmember Extraction is a critical step in hyperspectral image analysis and classification. It is an useful method to decompose a mixed spectrum into a collection of spectra and their corresponding proportions. In this paper, we solve a linear endmember extraction problem as an evolutionary optimization task, maximizing the Simplex Volume in the endmember space. We propose a standard genetic algorithm and a variation with In Vitro Fertilization module (IVFm) to find the best solutions and compare the results with the state-of-art Vertex Component Analysis (VCA) method and the traditional algorithms Pixel Purity Index (PPI) and N-FINDR. The experimental results on real and synthetic hyperspectral data confirms the overcome in performance and accuracy of the proposed approaches over the mentioned algorithms.\n\n")

	file.write('**Envirionment Setup:**\n\n')
	file.write('Monte Carlo runs: %s \n\n' % mrun)
	file.write('Number of endmembers to estimate: %s \n\n' % num_endm)
	file.write('Number of skewers (PPI): %s \n\n' % nSkewers)
	file.write('Maximum number of iterations (N-FINDR): %s \n\n' % maxit)

	
	file.write('### Parameters used in each GAEE versions\n\n')
	file.write(tabulate(tab3_conf, tablefmt="pipe", headers="keys")+'\n\n')

	file.write('### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SAM for the Cuprite Dataset.\n\n')
	file.write(tabulate(tab1_sam, tablefmt="pipe", headers="keys")+'\n\n')
	file.write('### Comparison between the ground-truth Laboratory Reflectances and extracted endmembers using PPI, N-FINDR, VCA, GAEE, GAEE-IVFm using SID for the Cuprite Dataset.\n\n')
	file.write(tabulate(tab2_sid, tablefmt="pipe", headers="keys")+'\n\n')

