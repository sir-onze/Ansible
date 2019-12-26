import fileinput;
import sys;

filename = '/Users/macz/Desktop/hosts'
f_teste = open("/Users/macz/Desktop/4ano/SDB/Ansible/testes/teste.txt","r")

lineStr = f_teste.readline();

for line in fileinput.FileInput(filename,inplace=1):
	if 'hotcrp.dev' in line:
		line = line.rstrip()
		line = line.replace(line,lineStr+" "+line+"\n")
	print line,