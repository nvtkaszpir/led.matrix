# LED matrix clock

## Requirements

- python 3
- raspberry 3
- Rasp Matrix 128 - 8x16 LED matrix shield based on MAX7219
- (optional) ntp set on Raspberry 3 with chrony


## Installation

- enable spi in rpi3, see [luma-led-matrix docs](https://luma-led-matrix.readthedocs.io/en/latest/install.html)
- install deps

```bash
# for development as pi user, required for older distros (pre-buster)
sudo usermod -a -G spi,gpio pi

# generic install
sudo apt-get update
sudo apt-get install -y chrony
sudo systemctl enable chrony
sudo systemctl start chrony

sudo apt install -y build-essential python3-dev python3-pip python3-virtualenv libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5 git

mkdir -p /home/pi/src
cd /home/pi/src/
git clone https://github.com/nvtkaszpir/led.matrix.git
cd led.matrix
python3 -m virtualenv .venv --python=python3
source .venv/bin/activate 
python3 -m pip install -r requirements.txt
sudo cp -f led-matrix-clock.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable led-matrix-clock
sudo systemctl start led-matrix-clock

```

## Known limitations

- when started another clock.py and then it is shut down then display is black, need to restart service
