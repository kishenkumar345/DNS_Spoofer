1. The target website chosen is youtube and can be pinged by typing either www.youtube.com or youtube.com

2. Start Kali Linux virtual machine. 

3. Place the DNS_spoof.py file into an easy to access folder.

4. Open a root terminal on the Kali Linux virtual machine. You may need to type your password for Kali to grant
you access to a root terminal.

5. Navigate to the directory where DNS_spoof.py is located using the "cd" command in the root terminal.

6. In the root terminal type the following commands in order, prior to anytime you run the program:
iptables --flush
iptables -I OUTPUT -j NFQUEUE --queue-num 1
iptables -I INPUT -j NFQUEUE --queue-num 1

7. In the root terminal type the following command to run the program:
python DNS_spoof.py

8. Open another normal terminal in your Kali Linux virtual machine.

9. Use either of the following commands to ping the target website youtube:
ping www.youtube.com
ping youtube.com

10. The root terminal prints information related to the modified DNS packet.
The normal terminal should print a response from the target website with the Kali Linux IP (attacker_IP).

11. Use ctrl+c to exit the program on the root terminal.

12. If a scapy import error occurs when trying to start the program, type the following commands in a terminal:
sudo mkdir /usr/lib/python2.7/dist-packages/scapy
cd /usr/lib/python3/dist-packages/
sudo cp -avr scapy/* /usr/lib/python2.7/dist-packages/scapy