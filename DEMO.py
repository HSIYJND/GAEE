	groundtruth = None
	y = None

	def load_groundtruth(self,gt_loc):
		pkg_gt = sio.loadmat(gt_loc)
		self.groundtruth = pkg_gt['Y']
		self.num_gtendm = self.groundtruth.shape[1]


	def plot_abundance(self, i):
		plt.matshow(self.abundances[:,:,i])

	def plot_groundtruth(self):
		plt.matshow(self.groundtruth[:,:])

if __name__ == '__main__':
	# data_loc = "./DATA/cuprite_data.mat"
	# data_loc = "./DATA/cuprite_groundtruth.mat"
	data_loc = "./DATA/grss2018_data.mat"
	gt_loc = "./DATA/grss2018_groundtruth.mat"
	num_endm = 20
	algo = VCA(data_loc,num_endm)
	algo.load_groundtruth(gt_loc)
	algo.extract_endmember()
	# vca.map_abundace()
	algo.FCLS()
	# vca.plot_abundance(1)	
	algo.plot_groundtruth()
	plt.show()