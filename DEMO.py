from VCA import *
from PPI import *
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

if __name__ == '__main__':
	# data_loc = "./DATA/cuprite_data.mat"
	# data_loc = "./DATA/cuprite_groundtruth.mat"
	data_loc = "./DATA/grss2018_data.mat"
	gt_loc = "./DATA/grss2018_groundtruth.mat"
	num_endm = 20
	verbose = True
	algo = 'VCA'

	vca = DEMO([data_loc,gt_loc,num_endm,algo],verbose)
	vca.extract_endmember()
	vca.map_abundance()
	vca.plot_endmember(0)
	vca.plot_abundance(0)
	plt.show()

	nSkewers = 100
	initSkewers = None
	algo = 'PPI'

	ppi = DEMO([data_loc,gt_loc,num_endm,algo,nSkewers,initSkewers],verbose)
	ppi.extract_endmember()
	ppi.map_abundance()
	ppi.plot_endmember(2)
	ppi.plot_abundance(2)
	plt.show()


	npop = 100
	ngen = 100
	cxpb = 0.3
	mutpb = 0.5
	algo = 'GAEE'
	
	gaee = DEMO([data_loc,gt_loc,num_endm,algo,npop,ngen,cxpb,mutpb],verbose)
	gaee.extract_endmember()
	gaee.map_abundance()
	gaee.plot_endmember(0)
	gaee.plot_abundance(0)
	plt.show()

	npop = 100
	ngen = 100
	cxpb = 0.3
	mutpb = 0.5
	algo = 'GAEE-IVFm'

	gaee = DEMO([data_loc,gt_loc,num_endm,algo,npop,ngen,cxpb,mutpb],verbose)
	gaee.extract_endmember()
	gaee.map_abundance()
	gaee.plot_endmember(0)
	gaee.plot_abundance(0)
	plt.show()
