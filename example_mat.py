# Upload a waveform from a .mat file to an AFG
# Author: Andrej Debenjak
#
# The create_waveform.m script should be run before this
# python script to create data.mat file, which is used by
# this python scrip

from tekusbtmc import TekUsbtmc
import scipy.io

# create TekUsbtmc instance
tek = TekUsbtmc()

# load data from data.mat
mat = scipy.io.loadmat('data.mat')
data = mat['waveform']
data = data[0][:].tolist();

# upload waveform to Tektronix AFG (at USER4 waveform memory),
# and verify the uploaded content
tek.upload_data(data, 'USER4', verify=True)

# close connection
tek.close()

