from Source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s_>%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_4_WaliPenilaian.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)