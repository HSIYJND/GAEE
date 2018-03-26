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
	p = None

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
		if argin[3] == 'GAEE':
			npop = argin[4]
			ngen = argin[5]
			cxpb = argin[6]
			mutpb = argin[7]
			if (verbose):
				print('... Selecting GAEE endmember extractor')
			self.ee = GAEE([self.data,self.nRow,self.nCol,self.nBand,self.nPixel, self.p, npop,
				ngen,cxpb,mutpb],self.verbose)

		if argin[3] == 'GAEE-IVFm':
			npop = argin[4]
			ngen = argin[5]
			cxpb = argin[6]
			mutpb = argin[7]
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

	def plot_groundtruth(self):
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

	def sam_matrix(self):
		data = np.asmatrix(self.data)		gt = self.groundtruth
		sam_m = np.zeros((self.p,self.num_gtendm));
		for i in range(0,self.p):
			sam_m[i,:] = self.SAM(data,gt[:,i])
		return sam_m

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
	# data_loc = "./DATA/cuprite_data.mat"
	# data_loc = "./DATA/cuprite_groundtruth.mat"
	data_loc = "./DATA/grss2018_data.mat"
	gt_loc = "./DATA/grss2018_groundtruth.mat"
	num_endm = 20
	verbose = False

	algo = 'VCA'

	vca = DEMO([data_loc,gt_loc,num_endm,algo],verbose)
	vca.extract_endmember()
	vca.sam_matrix()
	# vca.map_abundance()
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