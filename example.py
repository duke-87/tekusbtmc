# Simple example how to use tekusbtmc driver
# Author: Andrej Debenjak
from tekusbtmc import TekUsbtmc

tek = TekUsbtmc()

data = range(0,100)

tek.upload_data(data, 'USER4')

tek.close()

