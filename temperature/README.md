# Check tempetarute in the room 

## Use in this project 

1. RASPBERRY PI
- SoC: Broadcom BCM2837
- CPU: 4× ARM Cortex-A53, 1.2GHz
- GPU: Broadcom VideoCore IV
- RAM: 1GB LPDDR2 (900 MHz)
- Networking: 10/100 Ethernet, 2.4GHz 802.11n wireless
- Bluetooth: Bluetooth 4.1 Classic, Bluetooth Low Energy
- Storage: microSD
- GPIO: 40-pin header, populated
- Ports: HDMI, 3.5mm analogue audio-video jack, 4× USB 2.0, Ethernet, Camera - - Serial Interface (CSI), Display Serial Interface (DSI)
  
2. TWO DHT22 TEMPERATURE-HUMIDITY SENSOR(first inside, second outside)  
- Low cost
- 3 to 5V power and I/O
- 2.5mA max current use during conversion (while requesting data)
- Good for 0-100% humidity readings with 2-5% accuracy
- Good for -40 to 80°C temperature readings ±0.5°C accuracy
- No more than 0.5 Hz sampling rate (once every 2 seconds)
- Body size 15.1mm x 25mm x 7.7mm
- 4 pins with 0.1" spacing

3. Python 3.7
4. Adafruit_DHT library

## Raspberry Pi Humidity Software Installation and Testing
First of all, some packages have to be installed:

    sudo apt-get update
    sudo apt-get install build-essential python-dev python-openssl git

Now the library for the sensors can be loaded. I use a pre-built Adafruit library that supports a variety of sensors:

    git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT
    sudo python setup.py install

This creates a Python library that we can easily integrate into our projects.
If everything went well, we can already read the temperature and humidity. The easiest way is to first use the demo files:

    cd examples
    sudo ./AdafruitDHT.py 11 4

The first parameter (11) indicates which sensor was used (22 for the DHT22) and the second, to which GPIO it is connected (not the pin number, but the GPIO number). This produces an output like the following:

    $ sudo ./AdafruitDHT.py 11 4
    Temp=24.0*  Humidity=41.0%

Attention: The sensors are only ready every two seconds. Be careful not to start a query every second.

To integrate the Raspberry Pi humidity library into other (Python) projects, you only need the following:

    import Adafruit_DHT
    ...
    sensor = Adafruit_DHT.DHT11
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    ...