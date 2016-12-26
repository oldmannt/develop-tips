#### ssh
$service ssh start
config file in `/etc/ssh/sshd_config`

client:
$ssh username@ip or $ssh -p port_id ussername@ip

#### tornado
##### install
python3.5 
ubuntu 14
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5

ubuntu 15
sudo apt-get install python3.5

sudo cp /usr/bin/python /usr/bin/python_bak //backup
sudo rm /usr/bin/python                     //delete
sudo ln -s /usr/bin/python3.5 /usr/bin/python
python --version  // check version

download tornado
https://github.com/tornadoweb/tornado/releases
tar xvzf tornado-4.4.2.tar.gz
cd tornado-4.4.2
python3 setup.py build
sudo python3 setup.py install
