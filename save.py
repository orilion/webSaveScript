#! /usr/bin/python
import os
import sys
import time

date = time.strftime('%d-%m-%y %H:%M',time.localtime());

def verif(diretory,nbSave):
	exit = os.popen("ls -t "+diretory,"r").readlines();
	array = [line.rstrip('\n').split(',') for line in exit];
	if len(array) >= int(nbSave)
		str = "".join(array[len(array)-1]);
		os.system("rm -r "+diretory+"/"+str);

def save(nomHome,nomDB,nomSQL,nomTar,nbSave,password,diretory,user,host):
    diretory = diretory + "/" + nomHome;
	if os.path.exists(diretory) == False:
		os.mkdir(diretory);
	os.chdir(diretory);
	verif(diretory,nbSave);
	os.mkdir(str(date));
	os.chdir(str(date));
	os.system("tar cvzf \""+nomTar+".tar.gz\" /home/"+nomHome+"/www");
	os.system("mysqldump --no-tablespaces --host="+host+" --user="+user+" --password=\""+password+"\" "+nomDB+" > "+nomSQL+".sql");

try:
    nb = sys.arv.index("-p")
    password = sys.arv[nb+1]
except ValueError:
    print "-p is mandatory option with its value"
    exit(-1)
try:
    nb = sys.arv.index("-d")
    diretory = sys.arv[nb+1]
except ValueError:
    print "-d is mandatory option with its value"
    exit(-1)
try:
    nb = sys.arv.index("-conf")
    conf = sys.arv[nb+1]
except ValueError:
    print "-conf is mandatory option with its value"
    exit(-1)
try:
    nb = sys.arv.index("-u")
    user = sys.arv[nb+1]
except ValueError:
    user = "root"
try:
    nb = sys.arv.index("-host")
    host = sys.arv[nb+1]
except ValueError:
    host = "localhost"
os.chdir();
# read file
# format nomHome;nomDB;nomSQL;nomTar;nbSave
array = [line.rstrip('\n').split(';') for line in open(conf)];
for tab in array:
	save(tab[0],tab[1],tab[2],tab[3],password,diretory,user,host);
