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

#### aria2
##### install
```
apt-get update
apt-get install aria2
mkdir /root/aria2c  -p    //新建一个文件夹放置aria2的配置文件，如果路径中有不存在的文件夹，就加-p建立相应的路径
touch /root/aria2c/aria2.session //在该文件夹下建立一个session文件用于中断程序后的重新连接，出错时有用
touch /root/aria2c/aria2.conf // modify conf by sftp, conf will be showed below
```

aria2.conf file
```
#用户名
#rpc-user=
#密码
#rpc-passƒwd=
#上面的认证方式不建议使用,建议使用下面的token方式
#设置加密的密钥
rpc-secret=UVRad2zT7ykdgVsb
#允许rpc
enable-rpc=true
#允许所有来源, web界面跨域权限需要
rpc-allow-origin-all=true
#允许外部访问，false的话只监听本地端口
rpc-listen-all=true
#RPC端口, 仅当默认端口被占用时修改
#rpc-listen-port=8990
#最大同时下载数(任务数), 路由建议值: 3
max-concurrent-downloads=5
#断点续传
continue=true
#同服务器连接数
max-connection-per-server=5
#最小文件分片大小, 下载线程数上限取决于能分出多少片, 对于小文件重要
min-split-size=10M
#单文件最大线程数, 路由建议值: 5
split=10
#下载速度限制
max-overall-download-limit=0
#单文件速度限制
max-download-limit=0
#上传速度限制
max-overall-upload-limit=0
#单文件速度限制
max-upload-limit=0
#断开速度过慢的连接
lowest-speed-limit=0
#验证用，需要1.16.1之后的release版本
#referer=*
#文件保存路径, 默认为当前启动位置
dir=/root/downloads
input-file=/root/aria2c/aria2.session
save-session=/root/aria2c/aria2.session
save-session-interval=60
#文件缓存, 使用内置的文件缓存, 如果你不相信Linux内核文件缓存和磁盘内置缓存时使用, 需要1.16及以上版本
#disk-cache=0
#另一种Linux文件缓存方式, 使用前确保您使用的内核支持此选项, 需要1.15及以上版本(?)
#enable-mmap=true
#文件预分配, 能有效降低文件碎片, 提高磁盘性能. 缺点是预分配时间较长
#所需时间 none < falloc ? trunc << prealloc, falloc和trunc需要文件系统和内核支持
file-allocation=prealloc
```
##### web ui
```
$ wget https://github.com/ziahamza/webui-aria2/archive/master.zip
$ unzip master.zip
$ cp /root/webui/* /root/aria2/webui/    //直接复制脚本到LAMP的站点文件夹下（事先安装过LAMP）
//或者直接用Python做web服务器，更简单
cd /root/aria2/webui
$ nohup python -m SimpleHTTPServer 8991 &   //可以通过8991访问web ui
ln -s /root/downloads /root/aria2/webui/downloads
```
access by http://hostip:8991  
download the completed files by http://hostip:8991/downloads
