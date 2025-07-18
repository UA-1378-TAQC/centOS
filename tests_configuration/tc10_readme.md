# ⚙️ CentOS Script Repository for UA-1378 TAQC Students

This readme is written to help setup CentOS virtual machine up to TC10 Ip Address Blacklisting requirement

In this guide, gonna be non-optimal, but working solutions.
So Let`s GO.

## Network Setup

Make sure that your virtual machine is ont VMnet8 in her settings.

---

Then open cmd with admin rights on local machine and:
```cmd
ipconfig
```
You will see information about your connections and adapters. We are interesed in VMnet8 and VMnet1:
```cmd
Ethernet adapter VMware Network Adapter VMnet1:
Ethernet adapter VMware Network Adapter VMnet8:
```
By default, you connect to virtual machine using ip address from VMnet8. Our task is to connectn VMnet1 and VMnet8.


After that we goint to connect them:
```cmd
netsh interface ipv4 set interface "VMware Network Adapter VMnet1" forwarding=enabled
netsh interface ipv4 set interface "VMware Network Adapter VMnet8" forwarding=enabled
```
Then go to virtual machine`s cmd and enter:
```cmd
sudo ip route add IPv4 Address from VMnet1.0/24 via IPV4 Address from VMnet8.1
```
Example:
```cmd
sudo ip route add 192.168.171.0/24 via 192.168.229.1
```

To make sure that it worked, enter:
```cmd
ip route show
```
You will see something like that:
```cmd
default via 192.168.229.2 dev ens160 proto dhcp src 192.168.229.132 metric 100 
192.168.171.0/24 via 192.168.229.1 dev ens160 
192.168.229.0/24 dev ens160 proto kernel scope link src 192.168.229.132 metric 100
```
If that manual was written correctly, By now everything is gonna be ok and we can move to postfix ip blocklist setup.


## Postfix Setup

On that section we will setup postfix server to block request from ip.

---
On virtual machine open cmd and enter:
```cmd
sudo nano /etc/postfix/client_access
```

Enter ip from VMnet1 to move it into blacklist
```cmd
192.168.171.1   REJECT Blacklist Ip
```
Enter Ctrl + O to save and Ctrl + X to exit.

Then compile postfix server by:
```cmd
sudo postman /etc/postfix/client_access
```
Enter Ctrl + O to save and Ctrl + X to exit.

Go to main.cf and add line:
```cmd
sudo nano /etc/postfix/main.cf
smtpd_client_restrictions = check_client_access hash:/etc/postfix/client_access, permit
```
Enter Ctrl + O to save and Ctrl + X to exit.

Restart Postfix:
```cmd
sudo systemctl restart postfix
```

---

Congratulation!!! 
You successfully set up your virtual environment and now it`s ready to TC10 Ip Address Blacklisting test.
