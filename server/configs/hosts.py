import fileinput;
import sys;

filename = '/etc/hosts'
f_teste = open("/home/macz/ip.txt","r")

lineStr = f_teste.readline();

for line in fileinput.FileInput(filename,inplace=1):
	if 'hotcrp.dev' in line:
		line = line.rstrip()
		line = line.replace(line,lineStr+" "+line+"\n")
	print line,