from src import *
from fakeoption import *


from Register_Litmas import *
from Register_Pembimbingan import *
from Register_Pendampingan import *
from Register_Pengawasan import *


# @mark.looping
# def testoption():
# 	pilih = input('Masukan Nomer yang kan di Eksekusi \n'
# 		'1. Register Pendampingan \n'
# 		'2. Register Litmas \n'
# 		'3. Register Pembimbingan \n'
# 		'4. Register Pengawasan \n'
# 		'Masukan Nomor->>: '
# 	)

# 	if pilih == '2':
# 		for reg in range(17):
# 			try:
# 				testlitmas()
# 				testdatawbplitmas()
# 				testformtambahlitmas()
# 			except TimeoutError:
# 				print('ERRORR')
# 			reg = litmas + 1