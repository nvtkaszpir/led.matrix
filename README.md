# LED matrix clock

## Requirements

- python 3
- raspberry 3
- Rasp Matrix 128 - 8x16 LED matrix shield based on MAX7219
- (optional) ntp set on Raspberry 3


## Installation

- enable spi in rpi3, see [luma-led-matrix docs](https://luma-led-matrix.readthedocs.io/en/latest/install.html)
- install deps

```bash
sudo usermod -a -G spi,gpio pi
sudo apt-get update
sudo apt install build-essential python-dev python-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5 git
sudo pip3 install -r requirements.txt
mkdir -p /home/pi/src
cd /home/pi/src/
git clone https://github.com/nvtkaszpir/led.matrix.git
cd led.matrix
sudo cp led-matrix-clock.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable led-matrix-clock
sudo systemctl start led-matrix-clock
```
## Known limitations

- when started another clock.py and then it is shut down then display is black, need to restart service