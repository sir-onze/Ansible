import fileinput;
import sys;

filename = '/etc/mysql/mysql.conf.d/mysqld.cnf'
f_teste = open("/home/macz/ip.txt","r")
lineStr = f_teste.readline();

for line in fileinput.FileInput(filename,inplace=1):
	if 'bind-address            =' in line:
		line = line.rstrip()
		line = line.replace(line,line+" "+lineStr+"\n")
	print line,
