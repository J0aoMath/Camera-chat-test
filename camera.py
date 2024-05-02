from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

receiving = StreamingServer('192.168.0.17', 9999)
sending = CameraClient('192.168', 9999)
#Testes pendentes.

t1 = threading.Thread(target=receiving.start_server)
t1.start()

time.sleep(2) #bad habit code (synchronization)

t2 = threading.Thread(target=sending.start_streamcls)
t2.start()

while input('') != "STOP":
	continue

receiving.stop_server()
sending.stop_stream