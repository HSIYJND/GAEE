from VCA import *
from PPI import *
from NFINDR import *
from FIPPI import *
from GAEE import *
from GAEE_IVFm import *
from MAPS import *
import scipy.io as sio
import matplotlib.pyplot as plt

class DEMO(object):

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

	endmembers = None
	abundances = None

	verbose = True

	def __init__(self, argin,verbose):
		if (verbose):
			print('... Initializing DEMO')
		self.verbose = verbose
		self.load_data(argin[0])
		self.load_groundtruth(argin[1])
		self.data = self.convert_2D(self.data)
		
		self.p = argin[2]
		self.thr = argin[3]
		
		if argin[4] == 'VCA':
			if (verbose):
				print('... Selecting VCA endmember extractor')
			self.ee = VCA([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p],self.verbose)
		if argin[4] == 'PPI':
			nSkewers = argin[5]
			initSkewers = argin[6]
			if (verbose):
				print('... Selecting PPI endmember extractor')
			self.ee = PPI([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, nSkewers, initSkewers],self.verbose)
		if argin[4] == 'NFINDR':
			maxit = argin[5]
			if (verbose):
				print('... Selecting NFINDR endmember extractor')
			self.ee = NFINDR([self.data.T,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, maxit],self.verbose)
		if argin[4] == 'ATGP':
			if (verbose):
				print('... Selecting ATGP endmember extractor')
			self.ee = ATGP([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p],self.verbose)		
		if argin[4] == 'FIPPI':
			maxit = argin[5]
			if (verbose):
				print('... Selecting FIPPI endmember extractor')
			self.ee = FIPPI([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, maxit],self.verbose)	
		if argin[4] == 'GAEE':
			npop = argin[5]
			ngen = argin[6]
			cxpb = argin[7]
			mutpb = argin[8]
			if (verbose):
				print('... Selecting GAEE endmember extractor')
			self.ee = GAEE([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, npop,
				ngen,cxpb,mutpb],self.verbose)

		if argin[3] == 'GAEE-IVFm':
			npop = argin[5]
			ngen = argin[6]
			cxpb = argin[7]
			mutpb = argin[8]
			if (verbose):
				print('... Selecting GAEE-IVFm endmember extractor')
			self.ee = GAEEIVFm([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, npop,
				ngen,cxpb,mutpb],self.verbose)

		if (verbose):
			print('... Selecting NNLS abundance mapper')
		self.am = UCLS([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p],verbose)

	def extract_endmember(self):
		if (verbose):
			print('... Extracting endmembers')
		self.endmembers = self.ee.extract_endmember()

	def map_abundance(self):
		if (verbose):
			print('... Mapping abundances')
		self.am.endmembers = self.endmembers
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
		plt.plot(self.endmembers[:,i])
		plt.title(str(i))
		plt.xlabel('wavelength (µm)')
		plt.ylabel('reflectance (%)')
		plt.tight_layout()

	def SAM(self,a,b):
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
		[L, N] = s1.shape
		errRadians = np.zeros(N)
		s1 = np.asarray(s1)
		s2 = np.asarray(s2)
		for k in range(0,N):
			tmp = s1[:,k]
			p = (tmp / np.sum(tmp)) + np.spacing(1)
			q = (s2 / np.sum(s2)) + np.spacing(1)
			errRadians[k] = np.sum(p.T * np.log(p / q) + q * np.log(q / p))
		return errRadians

	def best_sam_match(self): # Best Estimated endmember for the groundtruth
		sam = np.zeros((self.num_gtendm,self.p))
		for i in range(self.endmembers.shape[1]):
			sam[i,:] = self.SAM(self.endmembers,self.groundtruth[self.selectedBands,:][:,i])

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

		newData = self.endmembers[:,new_idx]

		# self.endmembers = newData
		# print(new_value)

		return [newData, new_idx, new_value]

	def best_sid_match(self): # Best Estimated endmember for the groundtruth
		sid = np.zeros((self.num_gtendm,self.p))
		for i in range(self.endmembers.shape[1]):
			sid[i,:] = self.SAM(self.endmembers,self.groundtruth[self.selectedBands,:][:,i])
	
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

		newData = self.endmembers[:,new_idx]

		# self.endmembers = newData
		# print(new_value)

		return [newData, new_idx, new_value]

	def monte_carlo(self):
		print('Dh')

	def best_run(self,mrun,metric): # Monte Carlo Best Estimated EM with avg SAM or SID
		avg_run = 99999
		best_data = None
		for i in range(mrun):
			self.extract_endmember()
			if (metric == 'SAM'):
				[newData, new_idx, new_value] = self.best_sam_match()
			if (metric == 'SID'):
				[newData, new_idx, new_value] = self.best_sid_match()
			print(np.mean(new_value))
			if(np.mean(new_value) < avg_run):
				avg_run = np.mean(new_value)
				best_data = newData	
		print('BEST')
		print(np.mean(new_value))
	def best_overall(self): # Monte Carlo Best Estimated Member for All Runs
		print('Ch')

	def monte_carlo(gt,p_est,p,nBand,slectBands,thr,nRun):    
		gt = gt[slectBands,:]
		min_aux = np.ones(p)*100000
		all_scores = np.zeros((nRun,p))
		mc_result = np.asmatrix(np.zeros((nBand,p)))
		for i in range(nRun):
			##print ("Monte Carlo Run: ",i+1)
			S = algo(algo_argin)
			Sam = get_sam_matrix(S,gt,p_est,p)
			[nS, nIdx, SamScore] = cachassa_sam(S,Sam, p_est, p, thr)
			for k in range(p):
				if SamScore[k] < min_aux[k]:
					mc_result[:,k] = nS[:,k]
					min_aux[k] = SamScore[k]
		mc_result = np.asmatrix(mc_result)
		gt = np.asmatrix(gt)
		sam_scores = np.zeros(p)
		sid_scores = np.zeros(p)
		for l in range(mc_result.shape[1]):
			sam_scores[l] = SAM_aux(mc_result[:,l],gt[:,l])
			sid_scores[l] = SID_aux(mc_result[:,l],gt[:,l])

		return [mc_result,sam_scores, sid_scores]

if __name__ == '__main__':
	data_loc = "./DATA/cuprite_data.mat"
	gt_loc = "./DATA/cuprite_groundtruth.mat"
	# data_loc = "./DATA/grss2018_data.mat"
	# gt_loc = "./DATA/grss2018_groundtruth.mat"

	num_endm = 12
	verbose = False
	thr = 0.8
	mrun = 10
	metric = 'SAM'

	algo = 'VCA'

	vca = DEMO([data_loc,gt_loc,num_endm,thr,algo],verbose)
	vca.best_run(mrun,metric)
	# vca.extract_endmember()
	# vca.best_sam_match()
	# vca.map_abundance()
	# vca.plot_groundtruth(0)
	# vca.plot_endmember(0)
	# vca.plot_abundance(0)
	# vca.print_purepixels()
	# plt.show()

	# nSkewers = 100
	# initSkewers = None
	# algo = 'PPI'

	# ppi = DEMO([data_loc,gt_loc,num_endm,algo,nSkewers,initSkewers],verbose)
	# ppi.extract_endmember()
	# ppi.map_abundance()
	# ppi.plot_endmember(0)
	# ppi.plot_abundance(0)
	# ppi.print_purepixels()
	# plt.show()

	# maxit = 3*num_endm
	# algo = 'NFINDR'

	# nfindr = DEMO([data_loc,gt_loc,num_endm,algo,maxit],verbose)
	# nfindr.extract_endmember()
	# nfindr.map_abundance()
	# nfindr.plot_endmember(0)
	# nfindr.plot_abundance(0)
	# nfindr.print_purepixels()
	# plt.show()

	# npop = 100
	# ngen = 100
	# cxpb = 0.3
	# mutpb = 0.5
	# algo = 'GAEE'
	
	# gaee = DEMO([data_loc,gt_loc,num_endm,algo,npop,ngen,cxpb,mutpb],verbose)
	# gaee.extract_endmember()
	# gaee.map_abundance()
	# gaee.plot_endmember(0)
	# gaee.plot_abundance(0)
	# gaee.print_purepixels()
	# plt.show()

	# npop = 100
	# ngen = 100
	# cxpb = 0.3
	# mutpb = 0.5
	# algo = 'GAEE-IVFm'

	# gaee_ivfm = DEMO([data_loc,gt_loc,num_endm,algo,npop,ngen,cxpb,mutpb],verbose)
	# gaee_ivfm.extract_endmember()
	# gaee_ivfm.map_abundance()
	# gaee_ivfm.plot_endmember(0)
	# gaee_ivfm.plot_abundance(0)
	# gaee_ivfm.print_purepixels()
	# plt.show()

	# algo = 'ATGP'

	# fippi = DEMO([data_loc,gt_loc,num_endm,algo],verbose)
	# fippi.extract_endmember()
	# fippi.map_abundance()
	# fippi.plot_endmember(0)
	# fippi.plot_abundance(0)
	# fippi.show()

	# maxit = 10
	# algo = 'FIPPI'

	# fippi = DEMO([data_loc,gt_loc,num_endm,algo,maxit],verbose)
	# fippi.extract_endmember()
	# fippi.map_abundance()
	# fippi.plot_endmember(0)
	# fippi.plot_abundance(0)
	# fippi.show()