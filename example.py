from tekusbtmc import TekUsbtmc

tek = TekUsbtmc()

data = range(0,100)

tek.upload_data(data, 'USER4')

tek.close()

#tek.write_command('DATA:DELete:NAME EMEMory')

## USEFULL COMMANDS
# delete trace memory and EMEMory
        #self.write('DATA:DELete:NAME ' + trace_name)
        #self.write('DATA:DELete:NAME EMEMory')

 #self.write('DATA:DEFine EMEMory,' + str(10));


