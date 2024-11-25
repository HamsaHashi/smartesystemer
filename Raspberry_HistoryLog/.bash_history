New password: 
Retype new password: 
The password has not been changed.
passwd: Authentication token manipulation error
passwd: password unchanged
hamsahashi@raspberrypi:~ $ passwd hamsahashi
Changing password for hamsahashi.
Current password: 
New password: 
Retype new password: 
You must choose a longer password.
New password: 
Retype new password: 
passwd: password updated successfully
hamsahashi@raspberrypi:~ $ raspi-config
Script must be run as root. Try 'sudo raspi-config'
hamsahashi@raspberrypi:~ $ sudo raspi-config
Created symlink /etc/systemd/system/multi-user.target.wants/wayvnc.service → /lib/systemd/system/wayvnc.service.
hamsahashi@raspberrypi:~ $ sudo apt install realvnc-vnc-server
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
realvnc-vnc-server is already the newest version (7.11.0.18).
0 upgraded, 0 newly installed, 0 to remove and 157 not upgraded.
hamsahashi@raspberrypi:~ $ sudo systemctl start vncserver-x11-serviced.service
hamsahashi@raspberrypi:~ $ passwd hamsahashi
Changing password for hamsahashi.
Current password: 
passwd: Authentication token manipulation error
passwd: password unchanged
hamsahashi@raspberrypi:~ $ passwd hamsahashi
Changing password for hamsahashi.
Current password: 
passwd: Authentication token manipulation error
passwd: password unchanged
hamsahashi@raspberrypi:~ $ 
passwd: password unchanged
hamsahashi@raspberrypi:~ $ passwd hamsahashi
passwd hamsahashi
mount | grep '/'
sudo passwd hamsahashi
df -h
sudo update
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
sudo reboot
sudo raspi-config
sudo systemctl status
sudo systemctl start ssh
sudo systemctl enable ssh
sudo ufw allow ssh
sudo systemctl start vncserver-x11-serviced
tailscale ip
python3 --version
python3
which python3
python3
pip3 install torch torchvision torchaudio
pip3 install --upgrade pip
sudo apt update
sudo apt install build-essential cmake libopenblas-dev libx11-dev libgtk-3-dev libboost-python-dev
pip3 install --upgrade pip
sudo apt install python3-venv
python3 -m venv main-env
[200~source main-env/bin/activate
source main-env/bin/activate
pip install --upgrade pip
pip install ultralytics
pip install torch torchvision torchaudio
deactivate
which python3
source main-env/bin/activate
pip freeze > requirements.txt
deactivate
pip install -r requirements.txt
sudo apt install python3-numpy
sudo apt install python3-numpy python3-pandas python3-matplotlib
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential cmake libopenblas-dev liblapack-dev libx11-dev libgtk-3-dev libboost-python-dev
sudo apt install python3-pip
sudo pip3 install --upgrade pip
[200~sudo apt install python3-torch
sudo apt install python3-torch
sudo apt install python3-opencv python3-numpy
sudo pip3 install ultralytics
sudo apt update
sudo apt install git
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
python3 setup.py install
sudo apt install python3-numpy python3-opencv
sudo apt install python3-torch
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker pi
sudo usermod -aG docker hamsahashi
python3 -m ultralytics
sudo apt install python3-tqdm
docker run -it ultralytics/yolov5
sudo usermod -aG docker hamsahashi
logout
exit
groups hamsahashi
docker run hello-world
exit
sudo systemctl stop docker
[200~sudo apt remove docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo apt remove docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo apt autoremove
dpkg -l | grep python3-opencv
dpkg -l | grep python3-numpy
dpkg -l | grep python3-torch
sudo apt remove python3-opencv python3-numpy python3-torch
sudo apt autoremove
dpkg -l | grep python3-opencv
dpkg -l | grep python3-numpy
dpkg -l | grep python3-torch
sudo systemctl stop docker
sudo apt remove docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo apt autoremove
dpkg -l
sudo apt update
sudo apt upgrade
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo rm /etc/apt/sources.list.d/ros-latest.list
sudo apt-key del C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
cd Desktop/
cd SmarteSystemer/
git --help
git clone https://github.com/HamsaHashi/smartesystemer
git clone --help
ll
ls -l
cd smartesystemer/
ls -l
cd source/
ls -l
cd ../tensorflow_env/
ls -l
ls -l bin
pip install roboflow
pip --help
p3
py3
py -v
python3 --version
python -m venv smarteystemer
cd ../..
cd smartesystemer/
python -m venv smarteystemer
ls -l
rm smarteystemer/ -r
ls -l
cd tensorflow_env/
ls
ls -l
rm smarteystemer/
rm -r smarteystemer/
ls
cd ..
ls
cd ..
python -m venv smartesystemer-env
ll
ls 
cd smartesystemer
ls
cd ..
cd smartesystemer-env/
ls
cd ..
smartesystemer-env/bin/pip install roboflow
cd smartesystemer
git pull
tree ../
tree -help
tree --help
tree -d ../
ifconfig
smartesystemer-env/bin/pip install tensorflow
../smartesystemer-env/bin/pip install tensorflow
cd ..
cd smartesystemer-env/bin/
ls -l
./pip install tensorflow
pip install --upgrade pip setuptools wheel
./pip install --upgrade pip setuptools wheel
./pip install tensorflow
cd ~/Downloads/
ls -l
cat Miniforge3-Linux-aarch64.sh 
ls -l
./Miniforge3-Linux-aarch64.sh
sudo ./Miniforge3-Linux-aarch64.sh
bash Miniforge3-Linux-aarch64.sh 
conda --help
bash
conda --help
cd ../
ls -l
cd Downloads/
ls -l
bash Miniforge3-Linux-aarch64.sh 
cd ..
ls -l
miniforge3/
cd miniforge3/
ls -l
cd bin/
ls -l
conda --help
conda
ls -l
clear
ls -l
conda --help
ls -l
./conda
./conda init
ls
cd main-env
ls
cd ..
ls
cd smartesystemer
./get-docker.sh
sudo usermod -aG docker hamsahashi
docker ps
sudo systemctl unmask docker
sudo chmod 666 /var/run/docker.sock
pip3 -v install docker-compose
sudo pip3 -v install docker-compose
source /path/to/smarteSystemer-env/bin/activate
cd smartesystemer/
tree -d ../
cd smartesystemer-env/
cd smartesystemer-env
source smarteystemer/bin/activate
find / -name "bin/activate" 2>/dev/null
ls
pip list
cat ~/.bash_history | grep venv
source ~/main-env/bin/activate
pip list
deactivate 
source ~/smarteystemer/bin/activate
ls ~
find / -name "bin/activate"
pip show tensorflow roboflow ultralytics numpy opencv-python
sudo pip3 -v install docker-compose
sudo apt pip3 -v install docker-compose
sudo apt update
sudo apt install docker-compose
docker compose
sudo systemctl start docker
sudo init 6
sudo apt install python3-labelImg
pip install PyQt5 --prefer-binary
sudo apt-get install pyqt5-dev-tools
sudo pip3 install -r requirements/requirements-linux-python3.txt
pip cache purge
pip install PyQt5 --prefer-binary
pip cache purge
sudo docker pull tzutalin/labelimg
docker search labelImg
sudo apt install python3-pyqt5
git clone https://github.com/tzutalin/labelImg.git
cd labelImg
sudo apt install pyqt5-dev-tools
pip install -r requirements/requirements-linux-python3.txt
sudo apt install python3-distutils
pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install -r requirements/requirements-linux-python3.txt
conda install -c conda-forge distutils
pip install --upgrade setuptools
pip install -r requirements/requirements-linux-python3.txt
cd ..
sudo apt remove ros-*
sudo apt remove python3-pyqt5 pyqt5-dev pyqt5-dev-tools qt5-qmake qtbase5-dev qtchooser
pip uninstall labelImg PyQt5
pip cache purge
sudo apt reinstall python3-distutils
sudo reboot
sudo apt install python3-pyqt5
cd ~/labelImg
python3 labelImg.py
python labelImg.py
python3 labelImg.py
which python3
conda deactivate
which python3
python3 labelImg.py
sudo apt install python3-sip
conda deactivate
python3 labelImg.py
make all
cd ..
make all
ls
cd Desktop
ls
cd SmarteSystemer/
ls
cd ..
ls
pip install python3-pyqt5
sudo apt install python3-pyqt5
sudo apt autoremove
sudo apt install python3-pyqt5
pip install labelImg
pip3 install labelImg
pip install PyQt5
pip# install PyQt5
pip3 install PyQt5
sudo apt-get build-dep qt5-qmake
sudo apt-get build-dep libqt5gui5
sudo apt-get build-dep libqt5webengine-data
sudo apt-get build-dep libqt5webkit5
sudo apt-get install libudev-dev libinput-dev libts-dev libxcb-xinerama0-dev libxcb-xinerama0 gdbserver
pip install labelImg
rm -rf ~/labelImg
sudo apt-get remove --purge python3-pyqt5 python3-sip
sudo apt autoremove
sudo apt-get remove --purge libglu1-mesa libglu1-mesa-dev libqt5concurrent5 libqt5opengl5 libvulkan-dev qt5-qmake-bin
sudo apt autoremove
sudo apt clean
clear
sudo reboot
sudo apt update
[200~sudo nano /etc/apt/sources.list.d/ros-latest.list
sudo nano /etc/apt/sources.list.d/ros-latest.list
sudo apt update
sudo apt upgrade
sud apt install python3-pip
sudo apt install python3-pip
pip --version
pip3 --version
sudo pip install labelImg
cd Desktop
ls
cd SmarteSystemer/
ls
cd smartesystemer-env
ls
sudo pip install labelImg
sudo apt install labelImg
cd ..
sudo apt-get install pyqt5-dev-tools
sudo pip3 install -r requirements/requirements-linux-python3.txt
source ~/Desktop/SmarteSystemer/smartesystemer-env/bin/activate
conda deactivate
source ~/Desktop/SmarteSystemer/smartesystemer-env/bin/activate
conda deactivate
deactivate
source ~/Desktop/SmarteSystemer/smartesystemer-env/bin/activate
conda deactivate
conda config --set auto_activate_base false
conda deactivate
sudo apt install python3-pyqt5
ls
cd requirements.txt
nano ~/requirements.txt
cat ~/requirements.txt
pip-compile --generate-hashes --output-file=/home/hamsahashi/requirements.txt /home/hamsahashi/requirements.in
pip install pip-tools
pip-compile --generate-hashes --output-file=/home/hamsahashi/requirements.txt /home/hamsahashi/requirements.in
pip install -r requirements.txt --allow-unsafe
pip freeze > requirements.txt
pip install -r requirements.txt
conda activate
pip install -r requirements.txt
pip install -r requirements.txt --allow-unsafe
pip show setuptools
nano requirements.txt
grep setuptools requirements.txt
nano requirements.txt
history
sudo apt-get remove python3-labelImg
sudo apt-get autoremove
pip uninstall PyQt5
sudo apt-get remove pyqt5-dev-tools
sudo apt-get autoremove
sudo apt-get remove pyqt5-dev-tools
sudo apt-get autoremove
pip3 uninstall -r requirements/requirements-linux-python3.txt
pip uninstall -r requirements/requirements-linux-python3.txt
docker rmi tzutalin/labelimg
ls
git checkout -- requirements.txt
pip install -r requirements.txt
pip freeze
pip freeze > requirements.txt
nano requirements.txt
sudo reboot
source ~/Desktop/SmarteSystemer/smartesystemer-env/bin/activate
sudo apt-get install pyqt5-dev-tools
sudo pip3 install -r requirements/requirements-linux-python3.txt
brew install python3
pip3 install labelImg
pip install --upgrade pip
pip install labelImg
pip install --no-cache-dir labelImg
pip install --no-cache-dir --index-url=https://pypi.org/simple/ PyQt5 PyQt-builder
pip install --no-cache-dir --index-url=https://pypi.org/simple/ labelImg
sudo apt update
sudo apt full-upgrade
sudo apt install --reinstall python3-pip
python3 -m pip install --upgrade --force-reinstall pip
mkdir -p ~/.config/pip
nano ~/.config/pip/pip.conf
pip cache purge
sudo apt install --reinstall python3-pip
sudo apt update
sudo apt full-upgrade
sudo apt install --reinstall python3-pip
python3 -m pip install --upgrade --force-reinstall pip
mkdir -p ~/.config/pip
nano ~/.config/pip/pip.conf
sudo apt-get install pyqt5-dev-tools
sudo pip3 install -r requirements/requirements-linux-python3.txt
sudo apt-get update
sudo apt-get install python3-pyqt5
sudo apt-get install python3-lxml
git clone https://github.com/HumanSignal/labelImg.git
cd labelImg
sudo pip3 install -r requirements/requirements-linux-python3.txt
sudo apt-get install python3-full
pip install -r requirements/requirements-linux-python3.txt
mkdir -p ~/.config/pip
nano ~/.config/pip/pip.conf
which python
pip install -r /path/to/requirements.txt
ls
cd ..
ls
cd ~
rm -rf labelImg
ls
pip install -r ~/requirements.txt
pip install sympy==1.13.3
nano ~/requirements.txt
pip install pip-tools
pip-compile --generate-hashes --output-file ~/requirements.txt
pip install -r ~/requirements.txt
cp ~/requirements.txt ~/requirements.in
pip-compile --generate-hashes --output-file ~/requirements.txt ~/requirements.in
pip install -r ~/requirements.txt

pip install pip-tools
pip install -r ~/requirements.txt
pip-compile --generate-hashes --output-file ~/requirements.txt ~/requirements.in
sudo apt-get remove python3-labelImg
sudo apt-get autoremove
pip uninstall PyQt5
sudo apt-get remove pyqt5-dev-tools
sudo apt-get autoremove
sudo apt-get remove pyqt5-dev-tools
sudo apt-get autoremove
sudo apt-get remove pyqt5-dev-tools
sudo apt-get autoremove
pip3 uninstall -r requirements/requirements-linux-python3.txt
pip uninstall -r requirements/requirements-linux-python3.txt
docker rmi tzutalin/labelimg
ls requirements/
ls
ls requirements.txt/
rm requirements.txt
ls
rm requirements.in
ls
git checkout -- requirements.txt
ls
cd Desktop
ls
sudo apt update
sudo apt upgrade
sudo apt install python-dev python-pip
sudo apt install python3-dev python3-pip
sudo pip3 install --upgrade pip
cd Desktop
cd SmarteSystemer
ls
cd smartesystemer-env/
ls
activate
source Desktop/SmarteSystemer/smartesystemer-env/bin/activate
source ~/Desktop/SmarteSystemer/smartesystemer-env/bin/activate
pip install --upgrade pip
pip install tensorflow
sudo apt update
sudo apt install libhdf5-dev
pip install h5py
cd Desktop
ls
cd SmarteSystemer/
ls
ls -l
cd smartesystemer-env
ls -l
cd ..
ls
cd smartesystemer
ls
smartesystemer-env activate 
activate smartesystemer-env 
cd smartesystemer-env
activate
cd..
cd ..
ls
cd smartesystemer-env
activate
source ~/Desktop/SmarteSystemer/smartesystemer-env/bin/activate
clear
thonny
cd ..
ls
cd ..
ls
cd hamsahashi/
cd
ls
cd miniforge3
ls
[200~python3 -c "from ultralytics import YOLO; print('Ultralytics YOLO is installed')"
~
python3 -c "from ultralytics import YOLO; print('Ultralytics YOLO is installed')"
pip list
cd
pip list
pip show tensorflow
deactivate
pip show tensorflow
pip list
conda activate
pip list
pip show tensorflow
conda activate base
python
ls
cd Desktop
ls
cd SmarteSystemer/
ls
cd smartesystemer/
ls
cd..
cd ..
conda activate env-smartesystemer 
conda activate env_smartesystemer
ls -l
cd smartesystemer/
cd ~/Desktop/SmarteSystemer/smartesystemer/
ls -l
LS
ls
conda activate base
ls
pip list
conda list

pip 
cd Desktop/
ll
ls -l
cs SmarteSystemer/
ls -l
cd SmarteSystemer/
ls -l
cd smartesystemer
ls -l
conda --help
conda list
python
conda --help
pip --list
pip --help
pip list
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
python
conda activate base
conda create --name env_smartesystemer python=3.11
conda activate env_smartesystemer
conda install tensorflow
python --version
pip install tensorflow
bg
ls -l
cd ..
ls -l
cd smartesystemer
ls -l
git pull
git --help
git status
ls -l
cd ../smartesystemer-env/
ls -l
cd ..
rm smartesystemer -r
y
ls -l
rm smartesystemer-env/ -r
git clone https://github.com/HamsaHashi/smartesystemer
fg
bg
python --version
fg
conda install roboflow
conda install ultralytics numpy opencv
conda install anaconda::pyqt
pip install roboflow
conda list
conda remove opencv
pip install roboflow
python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
python
conda list
conda install conda-forge::ultralytics
python
conda install pytorch::pytorch
pip install torch
conda install ultralytics
conda install torch
conda install pytorch
python
conda install ultralytics-thop torchvision
conda install torchvision
pip install ultralytics-thop
python
bash
cd Desktop
ls
cd SmarteSystemer
ls
cd smartesystemer/
ls
cd ..
conda activate env_smartesystemer
python
cd Desktop
ls
cd SmarteSystemer/
ls
dc smartesystemer/
conda activate env_smartesystemer
python /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.14.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.14.1-linux-arm64/python_files/deactivate/bash/envVars.txt
source env_smartesystemer/bin/activate
conda activate env_smartesystemer
deactivate main-env
python /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.14.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.14.1-linux-arm64/python_files/deactivate/bash/envVars.txt
sudo reboot
sudo raspi-config
sudo nano /boot/config.txt
sudo nano /boot/firmware/config.txt
sudo reboot
sudo timedatectl set-time '2024-10-02 13:43:00'
conda activate env_smartesystemer
sudo apt update
1susb
lsusb
sudo apt install git
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
sudo ap install gcc-5
sudo apt install gcc-5
sudo timedatectl set-ntp true
date
sudo dpkg-reconfigure tzdata
date
git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
sudo apt install gcc-5
~cd
~ cd
sudo apt install build-essential
cd ~/DynamixelSDK/c/build/linux_sbc
make
sudo make install
cd ~/DynamixelSDK/c/example/protocol2.0/read_write/linux_sbc
make
sudo chmod a+rw /dev/ttyUSB0
cd ..
ls
cd python
ls
sudo python setup.py install
ls
lsusb
Bus 001 Device 009: ID fff1:ff48 CM-900   ROBOTIS Virtual COM Port
dmesg | grep tty
sudo raspi-config
ls /dev/tty*
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
sudo wpa_cli -i wlan0 reconfigure
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
ifconfig
sudo wpa_cli -i wlan0 reconfigure
sudo systemctl restart dhcpcd
lsls
cd Desktop
ls
cd SmarteSystemer/
ls
cd smartesystemer/
ls
conda activate env_smartesystemer
ls
cd
sudo systemctl restart NetworkManager
sudo systemctl list-units --type=service | grep network
sudo systemctl restart NetworkManager
sudo apt-get install dhcpcd5
sudo systemctl restart dhcpcd
sudo systemctl restart wpa_supplicant
sudo reboot
raspi-config
sudo raspi-config
sudo reboot
lxpanel --profile LXDE-pi
åpne spotify
ls
cd Desktop
ls
cd SmarteSystemer/
ls
cd smartesystemer/
ls
conda activate env_smartesystemer
ls
ipconfig
ifconfig
sudo wpa_cli -i wlan0 reconfigure
ifconfig
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
startx
ls ~Downloads
mv /home/hamsahashi/Downloads/best-pt /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam
ls ~Downloads
mv /home/hamsahashi/Downloads/best.pt /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam
cd Smartesystemer
ls
conda activate env_smartesystemer
ls
cd SmarteSystemer
cd /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam
ls
conda activate env_smartesystemer
cd SmarteSystemer/
cd smartesystemer/
ls
cd MyProjectHam
ls
/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
pip install opencv-python
sudo apt install opencv-python
source ~/Desktop/SmarteSystemer/smartesystemer/env_smartesystemer/bin/activate
conda activate env_smartesystemer
cd Smartesystemer
cd SmarteSystemer/
cd smartesystemer/
ls
cd MyProjectHam
ls
python3 RealTime_Ball_Detection.py
sudo apt-get update
sudo apt-get install libgtk2.0-dev pkg-config
sudo apt-get install libcanberra-gtk*
pip uninstall opencv-python
pip uninstall opencv-python-headless
pip install opencv-python
conda install -c conda-forge opencv
python3 RealTime_Ball_Detection.py
conda uninstall opencv libopencv py-opencv
conda install -c conda-forge opencv
python3 RealTime_Ball_Detection.py
pip install ultralytics
python3 RealTime_Ball_Detection.py
/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_ball_Detection.py
conda activate env_smartesystemer
cd SmarteSystemer/
cd smartesystemer/
cd MyProjectHam
nano RealTime_Ball_Detection.py
python3 RealTime_Ball_Detection.py
sudo nano ~/.config/lxsession/LXDE-pi/autostart
pip install opencv
ls
startx
sudo raspi-config
ping goggle
ping google.com
ping 1.1.1.1
sudo reboot
python
ls -la
mkdir Erik
cd Erik/
nano main.py
python main.py 
nano main.py
ifconfig
ping 1.1.1.1
sudo raspi-config
ifconfig
ping 1.1.1.1
startx
sudo apt list --installed | grep raspberrypi-ui-mods
sudo apt update
sudo raspi-config
ping google.com
sudo raspi-config
ping google.com
sudo raspi-config
ping google.com
sudo apt list --installed | grep raspberrypi-ui-mods
sudo apt update
sudo apt Run list --upgradable
sudo apt list --upgradable
sudo apt install raspberrypi-ui-mods
sudo raspi-config
xstart
startx
sudo apt update
sudo apt upgrade
sudo apt install -y wget
wget -0 code.deb https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64
wget -O  code.deb https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64
sudo apt install ./code.deb
wget  code.deb https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm64 -O code_arm64.deb
sudo apt install ./code_arm64.deb
sudo apt install ./<file>.deb
/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
conda activate env_systemer
conda activate env_smartesystemer
RealTime_Ball_Detection.py
ls
python3 RealTime_Ball_Detection.py
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
pip install python-dateutil
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
pip show python-dateutil
pip install ultralytics opencv-python python-dateutil
python RealTime_Ball_Detection.py
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python
python3 RealTime_Ball_Detection.py
pip install idna
python3 RealTime_Ball_Detection.py
source /home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/activate
hostname -I
python RealTime_Ball_Detection.py
ultralytics --version
(env_smartesystemer) hamsahashi@Hamsahashi:~/Desktop/SmarteSystemer/smartesystemer/MyProjectHam $ source /home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/activate
bash: /home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/activate: No such file or directory
(env_smartesystemer) hamsahashi@Hamsahashi:~/Desktop/SmarteSystemer/smartesystemer/MyProjectHam $ ls
pythong3 --version
python3 --version
idna --version
show idna
python RealTime_Ball_Detection.py
pip install --force-reinstall python-dateutil
pip install opencv-python-headless==4.10.0.84
conda uninstall opencv-python-headless
pip install opencv-python-headless==4.10.0.84
conda remove opencv-python-headless
pip install opencv-python-headless==4.10.0.84
conda remove opencv-python-headless
pip show opencv-python-headless
conda install -c conda-forge opencv-python-headless=4.10.0.84
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
sudo apt update
sudo apt upgrade
sudo apt install code -y
code
ifconfig
code
ls
cd Desktop
ls
cd SmarteSystemer/
cd smartesystemer/
ls
cd MyProjectHam/
LS
ls
code
conda activate env_smartesystemer
code
cd Desktop
cd SmarteSystemer/
cd smartesystemer/
ls
code
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
conda install -c conda-forge idna
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
python --version
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
cd Desktop/
cd SmarteSystemer/
cd smartesystemer/
conda activate env_smartesystemer
ls
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
sudo raspi-config
python
code
cd Desktop/SmarteSystemer/smartesystemer/
ls -l
cd MyProjectHam/
ls -l
python RealTime_Ball_Detection.py 
pip install ultralytics
pip install ultralytics --break-system-packages
python RealTime_Ball_Detection.py 
nano RealTime_Ball_Detection.py 
sudo apt install -y python3-picamera2
conda --help
ls
python RealTime_Ball_Detection.py 
ls -l
libcamera-hello
libcamera-hello --qt-preview
python RealTime_Ball_Detection.py 
apt-get install libxcb-xinput-dev
sudo apt-get install libxcb-xinput-dev
reboot
cd Desktop/
cd S
cd SmarteSystemer/
cd smartesystemer/
conda activate env_smartesystemer
ls
code
conda --help
conda list | grep cv
conda remove opencv
conda list | grep cv
conda status
conda
pip3 install opencv-contrib-python
sudo apt install python3-picamzero
code
python
pip list | grep cam
ifconfig
pip list
sudo apt update
3-picamzero
sudo apt install python3-picamzero
conda activate env_smartesystemer
python
sudo apt update && sudo apt ugrade
sudo apt upgrade
sudo apt install libcap-dev libatlas-dev ffmpeg libopenjp2-7
sudo apt install libcap-dev libatlas-base-dev ffmpeg libopenjp2-7
sudo apt install libcamera-dev
sudo apt install libkms++-dev libfmt-dev libdrm-dev
pip install --upgrade pip
pip install wheel
pip install rpi-libcamera rpi-kms picamera2
pip install rpi-libcamera
sudo apt install -y python3-picamera2
python
conda activate env_smartesystemer
conda deactivate 
/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
/bin/python
/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
code .
cd Desktop/
cd SmarteSystemer/
cd smartesystemer/
ls
code
python3 realtime_ball_detection.py
conda activate env_smartesystemer
python3 realtime_ball_detection.py
nano realtime_ball_detection.py
ls
cd MyProjectHam/
ls
python3 RealTime_Ball_Detection.py
nano RealTime_Ball_Detection.py
cd Desktop/SmarteSystemer/smartesystemer/
ls -l
cd MyProjectHam/
ls -l
python RealTime_Ball_Detection.py 
nano RealTime_Ball_Detection.py 
libcamera-hello --qt-preview
libcamera-hello
sudo raspi-config
uname -a
libcamera-hello
reboot
sudo apt update
ping google.com
sudo apt update
sudo apt upgrade
sudo apt update
ls
cd Desktop
ls
cd SmarteSystemer
ls
cd smartesystemer
ls
cd MyprojectHam
cd MyProjectHam
ls
code
sudo raspi-config
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
python3-picamera2
cd Desktop
ls
cd SmarteSystemer/
LS
ls
cd smartesystemer/
ls
cd MyProject
lsb_release -a
uname -a
cat/etc/os-release
congig
config
rasp-config
ifconfig
3-picamzero
sudo apt install -y python3-picamera2
show python3-picamera2
python3-picamera2 --version
find python3 --picamera2
find python3-picamera2
which python3-picamera2
whereis <python3-picamera2>
python3-picamera2 --version
python3 --version
picamera2 --version
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
conda deactivate
/home/hamsahashi/miniforge3/envs/env_smartesystemer/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
python3 --version
picamera2 --version
python3-picamera2 --version
sudo apt install -y python3-picamera2
sudo apt deinstall -y python3-picamera2
sudo apt remove -y python3-picamera2
cd ..
sudo apt remove -y python3-picamera2
cd Desktop/SmarteSystemer/smartesystemer/MyProjectHam
cd ..
cd Desktop/SmarteSystemer/smartesystemer/MyProjectHam
ls
python RealTime_Ball_Detection.py 
python -v
python --V
python -version
python --version
python -m venv --system-site-packages env
source env/bin/activate
ls
python RealTime_Ball_Detection.py 
sudo apt update && sudo apt upgrade -y
python RealTime_Ball_Detection.py 
sudo apt install -y python3-picamera2
python RealTime_Ball_Detection.py 
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
sudo update
sudo pt update
sudo apt update
sudo apt upgrade
code
sudo apt install -y python3-picamera2
python RealTime_Ball_Detection.py 
python3 RealTime_Ball_Detection.py 
ls
cd env/
ls
cd lib
ls
cd python3.11/
ls
cd site-packages/
ls
cd pip
ls
cd ..
apt install -y python3-picamera2
python
python3
pip install picamera2
cd ..
ls
pip install picamera2
python RealTime_Ball_Detection.py 
pip remove  picamera2
pip deinstall  picamera2
pip remove -y picamera2
pip -r picamera2
pip uninstall  picamera2
sudo apt install -y python3-libcamera python3-kms++
sudo apt install -y python3-prctl libatlas-base-dev ffmpeg python3-pip
sudo apt install -y python3-pyqt5 python3-opengl
pip3 install numpy --upgrade
pip3 install picamera2
pyton3 RealTime_Ball_Detection.py 
python3 RealTime_Ball_Detection.py 
pip3 deinstall picamera2
pip3 uninstall picamera2
pip3 install picamera2==0.3.12
python3 RealTime_Ball_Detection.py 
rpicam-hello
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/env/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
python3 RealTime_Ball_Detection.py 
python RealTime_Ball_Detection.py 
/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/env/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
pip uninstall python3-picam2
pip uninstall python3-picamera2
pip uninstall picamera2
/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/env/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/RealTime_Ball_Detection.py
rpicam-hello
sudo apt install -y python3-picamera2
python3 RealTime_Ball_Detection.py 
rpicam-hello
sudo apt remove -y python3-picamera2
rpicam-hello
python3 RealTime_Ball_Detection.py 
deactivate 
python3 RealTime_Ball_Detection.py 
sudo apt install -y python3-picamera2
python3 RealTime_Ball_Detection.py 
c
cd ..
exit'
exit()

dmesg | grep -i camera
cd Desktop
cd 
cd Desktop 
cd SmarteSystemer
cd smartesystemer
cd MyProjectHam
ls
dmesg | grep -i camera
ls
python test.py
ls
python test.py
openCV --version
cv2 --version
open.cv2 --version
python test.py
/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/env/bin/python /home/hamsahashi/test.py
python test.py
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
python test.py
rpicam-hello
python
pwd
ls
test.py
python test.py
vscode .
vscode
code .
python test.py
co
python test.py
code
python test.py
                                                                                                               /bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
servoer sier kjøøøøøøøør
ls
nano requirements.txt
cd initiation_dynamixel_arm/
ls
nano requirements.txt
cd ..
ls
nano requirements.txt
cd initiation_dynamixel_arm/
sudo pip3 install -r requirements.txt
sudo pip3 install -r requirements.txt --break-system-packages
cd ..
cd Desktop/
cd SmarteSystemer/smartesystemer/MyProjectHam/
ls
git clone ~https://github.com/Bakadeus/initiation_dynamixel_arm.git~
git clone https://github.com/Bakadeus/initiation_dynamixel_arm.git
cd initiation_dynamixel_arm/
sudo pip3 install -r requirements.txt --break-system-packages
code
python main.py
dmesg -w | grep tty
python3 main.py
ls
python3 main.py
cd ..
cd initiation_dynamixel_arm/
python3 main.py
cd ..
cd initiation_dynamixel_arm/
python3 main.py
python main.py
ll
exit
ll
cd Desktop/SmarteSystemer/smartesystemer/
git status
git push
sudo apt-get install git-gui
ll
ls -l
grep ll = <~/.bashrc
grep ll = ~/.bashrc
ll
bash
ls -alF
alias ll = 'ls -alF'
nano ~.bashrc
nano ~/.bashrc
bash
cd Desktop/
ls
cd SmarteSystemer/
cd smartesystemer/
cd MyProjectHam
python3 test.py
sudo reboot
ll
ls
ls -l
ll
cd Desktop/SmarteSystemer/smartesystemer/
git gui
bg
git config --global user.email "hamsaAbdikadir@hotmail.com"
git config --global user.name "HamsaHashi"
git status
git push
ping google.com
cd Desktop
ls
python3 test.py
ls
cd MyProjectHam/
python3 test.py
sudo shutdown -h no
cd Desktop/SmarteSystemer/smartesystemer/
cd ..
sudo shutdown -h now
ls
cd Desktop/
cd SmarteSystemer/smartesystemer/MyProjectHam/
ls
python test.py
python3 -m pip install pyserial
sudo pip3 python3 -m install pyserial --break-system-packages
python3 -m pip  install pyserial
python3 -m pip  install pyserial --break-system-packages
uname -m
cd Downloads/
ls
tar -xf arduino-1.8.19-linuxaarch64.tar.xz 
ls
sudo mv arduino-1.8.19 /opt/
ls
cd /opt/
ls
cd arduino-1.8.19/
ls
sudo ./install.sh
sudo shutdown -h now
ls
cd Arduino/
ls
cd ..
cd Desktop/
ls
ls /dev/tty*
clear
groupd
groups
raspi-config
rasp-config
sudo raspi-config 
clear
sudo apt install python3-pip
pip3 install pyserial
pip3 install pyserial --system-breake
sudo pip3 python3 -m install pyserial --break-system-packages
pip3 install pyserial --break-system-packages
pip3 show pyserial
clear
ls /dev/tty*
ls
ls /dev/tty*
ls ll
pip install python
ls /dev/tty*
ls
cd initiation_dynamixel_arm/
ls
245459
cd ..
cd Desktop/
cd SmarteSystemer/
cd smartesystemer/
ls
cd MyProjectHam/
ls
python test.py
ls /dev/tty*
sudo apt install keyboard
pip3  install keyboard --system-break-packages
pip3  install keyboard --break-system-packages
sudo pip3 install keyboard
pip3  install keyboard --break-system-packages
cd python_programs/
ls
sudo python3 Rasp_Arduino_Driving_Test.py
pip3  install keyboard --break-system-packages
sudo python3 Rasp_Arduino_Driving_Test.py
python3 Rasp_Arduino_Driving_Test.py
cd
sudo apt install pygame
pip install pygame --break-system-package
pip3  install keyboard --break-system-package
pip  install keyboard --break-system-package
cd python_programs/
python3 Rasp_Arduino_Driving_Test.py
sudo shutdown -h now
sudo bluetoothct1
sudo apt-get upgrade
sudo apt-get install joystick
sudo bluetoothct1
sudo bluetoothct 1
sudo bluetoothctl
sudo systemctl restart bluetooth
sudo bluetoothctl
sudo systemctl restart bluetooth
sudo bluetoothctl
python3 -m pygame --version
ls
python3 GameControll_Test.py 
sudo reebot
sudo reboot
ls /dev/tty*
cd python_programs/
python3 GameControll_Test_Com_Movements.py
cd Arduino/
ls
nano Arduino_Rasp_Driving_Test/
cd Arduino_Rasp_Driving_Test/
ls
nano Arduino_Rasp_Driving_Test.ino 
ls
cd python_programs/
ls
python3 GameControll_Test.py 
python3 GameControll_Test_Com_Movements.py 
ls /dev/tty*
ls
cd ..
cd python_programs/
ls
nano Rasp_Arduino_Driving_Test.py 
nano GameControll_Test_Com_Movements.py 
python3 GameControll_Test_Com_Movements.py 
ls
cd python_programs/
ls
cd Arduino/
LS
ls
ls
cd Desktop/
ls
cd SmarteSystemer/
cd smartesystemer/
ls
cd MyProjectHam/
ls
nano RealTime_Ball_Detection.py 
ls
cd python_programs/
ls
python3 GameControll_Test_Com_Movements.py 
nano GameControll_Test_Com_Movements.py 
python3 GameControll_Test_Com_Movements.py 
cd python_programs/
nano GameControll_Test_Com_Movements.py 
cd python_programs/
python3 GameControll_Test_Com_Movements.py 
cd python_programs/
python3 GameControll_Test_Com_Movements.py 
cd python_programs/
python3 GameControll_Test_Com_Movements.py 
cd Desktop
cd SmarteSystemer/smartesystemer/
cd MyProjectHam/
ls
nano test.py
cd ..
cd Arduino/
ls
nano Arduino_Rasp_Driving_Test/
conda deactivate
conda deactivate env
ls
Arduino_Rasp_Driving_Test/
cd Arduino_Rasp_Driving_Test/
ls
nano Arduino_Rasp_Driving_Test.ino 
/bin/python /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.16.1/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.16.1/python_files/deactivate/bash/envVars.txt
sudo apt install python3-picamera2 python3-socket
sudo apt install python3-picamera2
pip install numpy opencv-python
hostname -l
hostname -1
ifconfig
sudo apt install python3-picamera2 python3-socket
sudo apt install python3-socket
conda install python3-socket
conda install python3-sockets
sudo apt install python3-picamera2 python3-sockets
pip install sockets break--system-packages
pip install socket break--system-packages
pip install socket --break-system-packages
sudo apt install python3-picamera2 python3-socket --break-system-packages
iwlist wlan0 scan
sudo reebot'
sudo reboot
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf 
ifconfig 
ping google.com
ifconfig
cd Arduino_Rasp_Driving_Test/
cd python_programs/
cd Arduino_Rasp_Driving_Test/
ls
python3 GameControll_Test_Com_Movements.py 
cd ..
sudo apt install python3-picamera2
sudo apt autoremove
sudo apt -y python3-picamera2
pip3 uninstall picamera2
pip uninstall picamera2
sudo apt install -y python3-picamera2
sudo apt install -y python3-pyqt5 python3-opengl
python /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.16.1/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.16.1/python_files/deactivate/bash/envVars.txt
conda deactivate
ls
deactivate
ls
sudo reboot
ifconfig
ls
cd MyRaspberryPartUSS/
ls
cd python3/
ls
cd python_programs/
cd ..
cd python_programs/
ls
python3 GameControll_Test_Com_Movements.py 
deactivate
ls
cd MyRaspberryPartUSS/
ls
cd python3/
ls
python3 VideoSClient.py 
sudo apt update
sudo apt install python3-picamera2
sudo apt upgrade
cd ..
sudo shutdown -h now
python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
sudo shutdown -h now
ls
ls ll
ll
ls
cd python_programs/
ls
cd ..
ls
cd output
ls
cd ops
cd opt
cd /opt
raspi-config
sudo raspi-config
ipconfig
sudo ipconfig
ifconfig
/home/hamsahashi/main-env/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
conda deactivate main.env
conda deactivate main-env
conda deactivate
deactivate
/home/hamsahashi/main-env/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
python3 --version
/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
/usr/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
cd MyRaspberryPartUSS/
ls
cd python3/
ls
python3 VideoSClient.py 
which python3
cd ..
ls /usr/bin/python3*
/usr/bin/python3 --version
nano ~/.bashrc
source ~/.bashrc
which python3
python3 --version
which python3
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11.2
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
which python3
python3 --version
rm -rf /home/hamsahashi/main-env
which python3
python3 --version
sudo update-alternatives --config python3
which python3
/usr/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
pip install picamera2
pip3 install picamera2
python3 -m pip show picamera2
/usr/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
conda activate
/usr/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
python3 VideoSClient.py 
cd python3/
cd MyRaspberryPartUSS/
cd python3/
python3 VideoSClient.py 
conda deactivate
/usr/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
sudo apt install -y mjpg-streamer
sudo apt install -y cmake libjpeg8-dev gcc g++
sudo apt install -y cmake libjpeg62-turbo-dev gcc g++
git clone https://github.com/jacksonliam/mjpg-streamer.git
LS
ls
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install
mjpg_streamer -i "input_raspicam.so -fps 10 -x 640 -y 480" -o "output_http.so -w /usr/local/share/mjpg-streamer/www"
export LD_LIBRARY_PATH=/usr/local/lib/mjpg-streamer
mjpg_streamer -i "input_raspicam.so -fps 10 -x 640 -y 480" -o "output_http.so -w /usr/local/share/mjpg-streamer/www"
ls /usr/local/lib/mjpg-streamer
sudo apt install -y libraspberrypi-dev
cd ~/MyRaspberryPartUSS/python3/mjpg-streamer/mjpg-streamer-experimental
make clean
make
sudo make install
ls /usr/local/lib/mjpg-streamer
cd ~/MyRaspberryPartUSS/python3/mjpg-streamer/mjpg-streamer-experimental
make clean
mkdir _build
cd _build
cd ~/MyRaspberryPartUSS/python3/mjpg-streamer/mjpg-streamer-experimental/_build
ls
cmake -DENABLE_INPUT_RASPICAM=ON ..
rm -rf ~/MyRaspberryPartUSS/python3/mjpg-streamer
sudo rm -rf /usr/local/bin/mjpg_streamer
sudo rm -rf /usr/local/lib/mjpg-streamer
sudo rm -rf /usr/local/share/mjpg-streamer
ls /usr/local/bin/mjpg_streamer
ls /usr/local/lib/mjpg-streamer
ls /usr/local/share/mjpg-streamer
cd ..
ls
cd ..
ls
~/MyRaspberryPartUSS/python3/mjpg-streamer
cd ~/MyRaspberryPartUSS/python3/mjpg-streamer
git clone https://github.com/jacksonliam/mjpg-streamer.git
ls
cd ~/MyRaspberryPartUSS/python3/mjpg-streamer/mjpg-streamer-experimental
make
sudo make install
ls /usr/local/lib/mjpg-streamer
rm -rf ~/MyRaspberryPartUSS/python3/mjpg-streamer
sudo rm -rf /usr/local/bin/mjpg_streamer
sudo rm -rf /usr/local/lib/mjpg-streamer
sudo rm -rf /usr/local/share/mjpg-streamer
ls /usr/local/bin/mjpg_streamer
ls /usr/local/lib/mjpg-streamer
ls /usr/local/share/mjpg-streamer
cd ..
ls
clear
sudo apt install -y cmake libjpeg9-dev gcc g++ libcamera-dev git
sudo apt install -y cmake libjpeg62-turbo-dev gcc g++ libcamera-dev git
cd /opt
sudo git clone https://github.com/custom-build-robots/mjpg-streamer-rapi-libcamera.git
cd /opt/mjpg-streamer-rapi-libcamera/mjpg-streamer-experimental
sudo make
sudo make install
ls /usr/local/bin/mjpg_streamer
nano /opt/mjpg-streamer-rapi-libcamera/mjpg-streamer-experimental/plugins/input_libcamera/LibCamera.cpp
rm -rf ~/MyRaspberryPartUSS/python3/mjpg-streamer
sudo rm -rf /usr/local/bin/mjpg_streamer
sudo rm -rf /usr/local/lib/mjpg-streamer
sudo rm -rf /usr/local/share/mjpg-streamer
ls
cd ..
sudo rm -rf /opt
ls
cd ..
ls
cd ..
ls
clear
sudo apt install -y libcamera-apps ffmpeg
cd MyRaspberryPartUSS
ifconfig
/usr/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/VideoSClient.py
cd MyRaspberryPartUSS
sudo apt install -y libcamera-apps ffmpeg
libcamera-vid --help
ffmpeg -version
libcamera-vid -t 0 --width 1280 --height 720 --framerate 15 --nopreview --listen -o tcp://0.0.0.0:8554
hostname -l
hostname -1
hostname -i
hostname -I
libcamera-vid -t 0 --width 1280 --height 720 --framerate 15 --nopreview --listen -o tcp://0.0.0.0:8554
sudo lsof -i :8554
libcamera-vid -t 0 --width 1280 --height 720 --framerate 15 --nopreview --listen -o tcp://0.0.0.0:8555
ps aux | grep libcamera-vid
sudo pkill libcamera-vid
ps aux | grep libcamera-vid
sudo reboot
python /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.16.1/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.16.1/python_files/deactivate/bash/envVars.txt
top
libcamera-vid -t 0 --width 1280 --height 720 --framerate 15 --nopreview --listen -o tcp://0.0.0.0:8554
hostname -I
libcamera-vid -t 0 --width 1280 --height 720 --framerate 15 --nopreview --listen -o tcp://0.0.0.0:8554
libcamera-vid -t 0 --width 1280 --height 720 --framerate 15 --nopreview --listen -o tcp://0.0.0.0:8554
libcamera-vid -t 0 --width 640 --height 480 --framerate 10 --nopreview --listen -o tcp://0.0.0.0:8554
libcamera-hello -t
libcamera-hello -t o
libcamera-vid -t 0 --inline -n -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream}' :demux=h264
libcamera-vid -t 0 --inline -n -o - | cvlc stream:///dev/stdin --sout '#std{access=http,mux=ts,dst=:8554/stream}' :demux=h264
clear
libcamera-vid -t0 --width 1920 --height 1080 --framerate 10 --nopreview --codec h264 --profile high --intra 5 --listen -o tcp://0.0.0.0:8494
libcamera-vid -t0 --width 1920 --height 1080 --framerate 10 --nopreview --codec h264 --profile high --intra 5 --listen -o tcp://0.0.0.0:8554
sudo shutdown -h now
sudo apt update
sudo raspi-config
ls
cd python3/
python3 stream.py
ngrok http http://localhost:8080
/bin/python
/bin/python /home/hamsahashi/MyRaspberryPartUSS/python3/stream.py
ls
cd python3/
python stream.py
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc 	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null 	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" 	| sudo tee /etc/apt/sources.list.d/ngrok.list 	&& sudo apt update 	&& sudo apt install ngrok
ngrok config add-authtoken 2lq24V5DUTayMgXBm5xROlCBBHI_6X1M2KZyxhZqt4V5RZR2L
ngrok http http://localhost:8080
pip install opencv-python
pip install opencv-python --break-system-packages
sudo -h shutdown
sudo  shutdown
sudo shutdown .h
sudo shutdown -h
-c
shutdown -c
ls
sudo shutdown -h now
ngrok http http://localhost:8080
ls
cd MyRaspberryPartUSS/
ls
cd Arduino/
ls
python3 -m venv --system-site-packages yolo_object
source yolo_object/bin/activate
sudo apt update
sudo apt upgrade
pip install -U pip
sudo apt install python3-pip -y
pip install ultralytics[export]
reboot
df -h
du -h /dev/mmcblk0p2
df -h /dev/mmcblk0p2
cd dev
/home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/env/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/test.py
deactivate
/bin/python /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode/extensions/ms-python.python-2024.16.1-linux-arm64/python_files/deactivate/bash/envVars.txt
cd Desktop/SmarteSystemer/smartesystemer/MyProjectHam/
python3 test.py
cd ..
ls
cd Desktop/
ls
cd SmarteSystemer/
cd smartesystemer
ls
cd MyProjectHam/
ls
python3 RealTime_Ball_Detection.py 
ls
python test.py
/bin/python3.11
cd SmarteSystemer/smartesystemer/MyProjectHam/YOLO\ Object\ Detection/
cd ..
ls
cd YOLO\ Object\ Detection/
python3 ncnn_yolo_converter.py 
cd Desktop/
ls
cd yolo\ object\ detection/
ls
cd python_programs/
ls
nano GameControll_Test_Com_Movements.py 
ls
cd python_programs/
ls
cd ..
cd Desktop/
ls
cd SmarteSystemer/smartesystemer/
ls
cd MyProjectHam/
ls
cd ..
ls
cd ..
ls
cd MyRaspberryPartUSS/
ls
cd Arduino/
ls
cd Testfiler\ Arduino/
ls
nano Arduino_BI__Raspberry_Front_Back_Communication/
cd Arduino_BI__Raspberry_Front_Back_Communication/
LS
ls
nanano Arduino_BI__Raspberry_Front_Back_Communication.ino 
nano Arduino_BI__Raspberry_Front_Back_Communication.ino 
cd ..
ls
cd Arduino_Rasp_Driving_Test/
ls
nano Arduino_Rasp_Driving_Test.ino 
cd ..
ls
cd python3/
ls
cd Kaos_samling/
ls
cd ..
ls
cd python_programs/
ls
nano GameControll_Test_Com_Movements.py 
ngrok --http hamsahashi.ngrok.dev 8080
ngrok http 8080 --http hamsahashi.ngrok.dev
ngrok http --http hamsahashi.ngrok.dev 8080
ngrok http --http://hamsahashi.ngrok.dev 8080 
ngrok http --http hamsahashi.ngrok.dev 8080
ngrok http --url hamsahashi.ngrok.dev 8080
cd yolo\ object\ detection/
python CameraCaptureImage.py 
ls /dev/tty*
sudo reebot
sudo reboot
ls /dev/tty*
cd /tmp/arduino_cache_343515/
ls
cd core
ls
rm core_arduino_avr_mega_cpu_atmega2560_1621df717313d057c92202babd71649a.a 
ls
cd ..
ls
cd ..
ls
ls /dev/tty*
cd yolo_object
cd python_programs
cd arduino
cd /opt/arduino-*
which arduino
sudo apt remove --purge arduino
rm -rf ~/tmp/arduino_cache_*
rm -rf ~/tmp/arduino15
rm -rf ~/tmp/arduino
ls /usr/bin/arduino
locate arduino
rm -rf ~/Desktop/arduino.desktop
rm -rf ~/Desktop/arduino*
find ~/Desktop -name "*arduino*"
which arduino
arduino
rm -rf ~/.arduino15
rm -rf ~/.arduino
rm -rf ~/tmp/arduino_cache_'
rm -rf ~/tmp/arduino_cache_*
exit()
rm -rf ~/tmp/arduino_cache_*
rm ~/Desktop/arduino-arduinoide.desktop
sudo rm /usr/share/applications/arduino-arduinoide.desktop
sudo find / -name "*arduino*"
sudo rm -rf /usr/share/arduino
sudo rm -rf /usr/bin/arduino
sudo rm -rf /usr/bin/arduino-ctags
sudo rm -rf /usr/bin/arduino-builder
sudo rm -rf /usr/local/bin/arduino
rm -rf ~/.arduino15
rm -rf ~/Arduino
rm -rf /tmp/arduino_cache_*
sudo rm -rf /usr/share/applications/arduino-arduinoide.desktop
rm -rf ~/Desktop/arduino-arduinoide.desktop
sudo rm -rf /root/Desktop/arduino-arduinoide.desktop
sudo find /usr/share/icons -name "*arduino*" -exec rm -rf {} \;
sudo find /usr/share/mime -name "*arduino*" -exec rm -rf {} \;
sudo find /usr/share/man -name "*arduino*" -exec rm -rf {} \;
sudo find /usr/share/doc -name "*arduino*" -exec rm -rf {} \;
rm -rf ~/Downloads/arduino-1.8.19-linuxaarch64.tar.xz
sudo find / -name "*arduino*"
sudo rm -rf /usr/share/lintian/overrides/arduino-core-avr
sudo rm -rf /usr/share/lintian/overrides/arduino-ctags
sudo rm -rf /usr/share/lintian/overrides/arduino-builder
sudo rm -rf /usr/share/arduino-builder
sudo rm -rf /var/lib/dpkg/info/arduino-ctags.*
sudo rm -rf /var/lib/dpkg/info/arduino-core-avr.*
sudo rm -rf /var/lib/dpkg/info/arduino-builder.*
sudo rm -rf /usr/share/lintian/overrides/arduino-core-avr
sudo rm -rf /usr/share/lintian/overrides/arduino-ctags
sudo rm -rf /usr/share/lintian/overrides/arduino-builder
sudo rm -rf /usr/share/arduino-builder
sudo rm -rf /var/lib/dpkg/info/arduino-ctags.*
sudo rm -rf /var/lib/dpkg/info/arduino-core-avr.*
sudo rm -rf /var/lib/dpkg/info/arduino-builder.*
sudo rm -rf /var/lib/dpkg/info/arduino-core-avr.*
sudo rm -rf /var/lib/dpkg/info/arduino-ctags.*
sudo rm -rf /usr/share/arduino-builder
sudo rm -rf /usr/share/lintian/overrides/arduino-builder
sudo rm -rf /usr/share/lintian/overrides/arduino-ctags
sudo rm -rf /usr/share/lintian/overrides/arduino-core-avr
sudo rm -rf /var/lib/dpkg/info/arduino-builder.*
sudo find / -name "*arduino*"
ls ~/.local/share/Trash
ls
cd  ~/.local/share/Trash
ls
cd files/
ls
ls ~/.local/share/Trash/files
rm -rf ~/.local/share/Trash/files/*
rm -rf ~/.local/share/Trash/info/*
ls
ls ~/.local/share/Trash/info
cd ..
ls
cd info
ls
cd ..
ls
cd desktop-directories/
ls
cd ..
ls
cd ..
deborphan
df -h
sudo du -ahx / | sort -rh | head -20
cd ~/Downloads/arduino-1.8.19
cd arduino-1.8.19/
cd arduino-1.8.19
cd Downloads/
cd arduino-1.8.19
cd arduino-1.8.19/
ls
cd ~/Downloads/arduino-1.8.19
cd arduino-1.8.19-linuxaarch64.tar.xz
cd ..
cd Desktop/
wget https://downloads.arduino.cc/arduino-1.8.19-linuxarm.tar.xz
tar -xf arduino-1.8.19-linuxarm.tar.xz
cd arduino-1.8.19
sudo ./install.sh
arduino
ls
sudo ./install.sh
arduino
sudo apt install default-jdk
arduino
cd Desktop/arduino-1.8.19/java/bin/
ll
sudo arduino
ll
readlink
readlink -f java 
java
arduino
/home/hamsahashi/Desktop/arduino-1.8.19/java/bin/java
dir
ls
path
pwd
/home/hamsahashi/Desktop/arduino-1.8.19/java/bin/java
java
cd ..
bin/java 
cd bin
java
arduino
cd ../../..
ls
ll
cd arduino-1.8.19/
ls -l
uninstall.sh
./uninstall.sh 
sudo ./uninstall.sh 
ls
arduino
sudo ./install.sh 
cat arduino-linux-setup.sh 
arduino
./java/bin/java 
./uninstall.sh 
sudo ./uninstall.sh 
sudo apt install arduino
arduino
ll
cd ..
bash
python printFilinnehold.py 
python /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.20.0-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.20.0-linux-arm64/python_files/deactivate/bash/envVars.txt
python /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.20.0-linux-arm64/python_files/printEnvVariablesToFile.py /home/hamsahashi/.vscode-server/extensions/ms-python.python-2024.20.0-linux-arm64/python_files/deactivate/bash/envVars.txt
/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/UUS_main.py
/usr/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/UUS_main.py
touch smartesystemer/MyProjectHam/USSmodules/__init__.py
touch smartesystemer/MyProjectHam/USSconfig/__init__.py
/usr/bin/python /home/hamsahashi/Desktop/SmarteSystemer/smartesystemer/MyProjectHam/UUS_main.py
top
python -c "import ncnn; print('ncnn installed successfully')"
ls
cd Desktop/
ls
cd SmarteSystemer/smartesystemer/
ls
cd MyProjectHam/
ls
cd MyRaspberryPartUSS/
ls
cd python_programs/
ls
python GameControll_Test_Com_Movements.py 
nano GameControll_Test_Com_Movements.py 
cd Desktop/SmarteSystemer/smartesystemer/
ls
cd MyProject
cd MyProjectHam/
ls
cd MyRaspberryPartUSS/
ls
cd python_programs/
ls
python3 newTestOMNIDrive.py
nano newTestOMNIDrive.py
python3 newTestOMNIDrive.py
nano newTestOMNIDrive.py
python newTestOMNIDrive.py
cd smartesystemer/
ls
cd MyProjectHam/
ls
cd MyRaspberryPartUSS/
ls
cd python_programs/
ls
python newTestOMNIDrive.py
