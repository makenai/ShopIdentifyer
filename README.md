Setup (Development)
===

1. Requirements
  * Python 2.7.x
  * virtualenv 1.11.x
  * MySQL 5.6.x
  * USB / Serial RFID Reader (see below)


2. Set up a python virtual environment, grab the source and pip install the requirements.txt file included:

        $ mkvirtualenv ShopIdentifyer
        $ workon ShopIdentifyer
        $ cd ShopIdentifyer
        $ pip install -r requirements.txt

3. Additionally, the system needs a ./identity/config.py file with the following properties:

        ENCRYPTED_STRIPE_TOKEN = 'encrypted-token'
        ENCRYPTED_DATABASE_PASSWORD = 'encrypted-password'

        DATABASE_USER = 'root'
        DATABASE_HOST = 'localhost'
        DATABASE_PORT = 3306
        DATABASE_SCHEMA = "shopidentifyer"

        STRIPE_CACHE_REFRESH_MINUTES=60

Please not that <span style="background-color:#FFD700">some of these properties are encrypted.  When the web server starts up, it will prompt you for a decryption password.</span>  This is the same password that you will use to encrypt the properties using the tool in ./identity/crypto/crypt.py.  The instructions for use are pretty straightforward:

    $ python crypt.py

    Usage: crypt.py enc <plaintext> <passphrase>
    crypt.py dec <encrypted> <passphrase>



The Serial Remote
===
In addition to the Flask web application, there is an out of process daemon that listens for incoming
RFID swipes on a given serial port, and then pushes them into the system.

The daemon is located in ./serial_remote/serial_listener.py and can be started as follows:

    $ python serial_remote/serial_listener.py start

Please note that this assumes you have already set up a virtualenv with the requirements.txt satisfied.

Inside of ./serial_remote/config.py, you can change the value for the RFID serial device.  My reader shows up as:

    /dev/tty.usbserial-A800509r



The RFID Reader
===

IN PROGRESS
