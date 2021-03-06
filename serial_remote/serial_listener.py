import serial
import time,sys

import requests

import config
from daemon import Daemon

class SerialListener(Daemon):

    def run(self):

        ser = serial.Serial(config.SERIAL_DEVICE, config.SERIAL_BAUD_RATE, timeout=1)

        while 1:

            try:
                time.sleep(1)
                str1 = ser.readline()

                if len(str1) > 3:
                    s = str1.lstrip('\x02').rstrip()
                    payload = {"message":s}
                    r = requests.put(config.MESSAGE_QUEUE,data=payload)

            except:
                pass

if __name__ == '__main__':

    daemon = SerialListener('/tmp/serial_listener.pid')

    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
            sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
