#import time
#from struct

class TekUsbtmc:
    USBTMC_USR_WAVEFORM_NAME = ['USER1', 'USER2', 'USER3', 'USER4']
    
    def __init__(self, device="/dev/usbtmc0"):
        self.usbtmc = open(device, mode = "r+", buffering=0)
        self.device = device
        self.id = self.get_id()
        print('Connected to: %s' % self.id)
        
    def close(self):
        self.usbtmc.close()
        
    def write(self, string):
        self.usbtmc.write(string)
        #time.sleep(0.01)

    def read(self):
        return self.usbtmc.readline().strip()
    
    def get_id(self):
        self.write('*IDN?')
        return self.read()
    
    def get_value(self, index):
        if index < 1:
            print 'Index should starts with 1!'
            return -1
        
        self.write('DATA:DATA:VALue? EMEMory,' + str(index))
        try:
            st = self.read()
        except:
            return -1
        
        return int(st)
        
        
    def upload_data(self, data, usr_wav_name, verify = True):
        #trace name: USER1 USER2 USER3, USER4
        if not any(True for name in self.USBTMC_USR_WAVEFORM_NAME if name == usr_wav_name):
            print 'Wrong USER waveform name. Possible options:'
            print self.USBTMC_USR_WAVEFORM_NAME
            return
        
        length = len(data)
        # check if length of the input data is appropriate (2--131072)
        if (length < 2) or (length > 131072):
            print 'The length of the input data is out of bonds!'
            print 'The length should be between 2 and 131072 (now it is ' + str(length) + ').'
            return
        
        # check if data is in the required interval (0--16382)
        for x in data:
            if (x < 0) or (x > 16382):
                print 'Input data out of range!'
                print 'input data shoult contain values between 0 and 16382.'
                return

        # prepare the header of the command
        #header = 'DATA:DATA EMEMory,#' + str(len(str(length*2))) + str(length*2)
        header = 'DATA:DATA EMEMory,#6' + '{:06d}'.format(length*2)

        # prepare the binary data
        binary_data = ''
        for i in range(0,length):
            binary_data += chr(( (data[i] >> 8 ) & 0x000000FF ))    #lower byte
            binary_data += chr( data[i] & 0x000000FF )              #higher byte
            
        #binary_data = struct.pack('>' + 'h'*len(data), *data)

        # transfer data to device
        print 'Transfering data...'
        self.write( header + binary_data)

        # copy data to trace
        self.write('DATA:COPY '+ usr_wav_name + ',EMEMory')
        
        # verify the integrity
        if verify:
            print 'Verifying data...'
            for i in range(0,length):
                val = self.get_value(i+1)
    
                if val != data[i]:
                    print 'Value at #' + str(i+1) + ' is incorrect! To fix this, try to resend the data.'
                    return
                
            print 'Data transferred successfully.'
        else:
            print 'Data transferred, but not verified'
        
        
            
            
    def set_value(self, index, data):
        if index < 1:
            print '\n\rIndex starts with 1!\n\r'
            return
        
        if (data < 0) or (data > 16382):
            print '\n\rInput data out of range!'
            print 'input data shoult contain values between 0 and 16382.\n\r'
            return
        
        self.write('DATA:DATA:VALue EMEMory,' + str(index) + ',' + str(data))
        val = self.get_value(index)
        
        if val != data:
            print 'Transfer failed!'
        else:
            print 'Value transfered sucessfully.'
    