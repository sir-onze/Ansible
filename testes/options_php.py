import fileinput;
import sys;

filename = '/Users/macz/Desktop/options.php'
f_teste = open("/Users/macz/Desktop/4ano/SDB/Ansible/testes/teste.txt","r")
lineStr = f_teste.readline();

for line in fileinput.FileInput(filename,inplace=1):
	if '$Opt["dbHost"] =' in line:
		line = line.rstrip()
		line = line.replace(line,line+"\""+lineStr+"\""+";")
	print line,
