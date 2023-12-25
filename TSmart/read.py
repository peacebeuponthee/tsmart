import logging, socket, sys
from settings import TSmartSettings
from time import sleep
from logging.handlers import TimedRotatingFileHandler

if TSmartSettings.Log_Level.lower()=="debug":
    if TSmartSettings.Debug_File_Location=="":
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler()])
    else:
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler(),TimedRotatingFileHandler(TSmartSettings.Debug_File_Location, when='D', interval=1, backupCount=7)])
elif TSmartSettings.Log_Level.lower()=="info":
    if TSmartSettings.Debug_File_Location=="":
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler()])
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler(),TimedRotatingFileHandler(TSmartSettings.Debug_File_Location, when='D', interval=1, backupCount=7)])
else:
    if TSmartSettings.Debug_File_Location=="":
        logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler()])
    else:
        logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(name)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler(),TimedRotatingFileHandler(TSmartSettings.Debug_File_Location, when='D', interval=1, backupCount=7)])


logger = logging.getLogger("TSmart_Read")

def controlRead():
    logger.info("Sending Control Read message")
    msgFromClient= [241,0,0,164]
    bytesToSend = bytearray(msgFromClient)
    serverAddressPort= (TSmartSettings.IP_Address, 1337)
    bufferSize= 1028

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)


while True:
    controlRead()
    sleep (TSmartSettings.self_run_timer)
