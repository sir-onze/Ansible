import fileinput;
import sys;

filename = '/var/www/hotcrp/conf/options.php'

for line in fileinput.FileInput(filename,inplace=1):
	if '$Opt["dbHost"] =' in line:
		line = line.rstrip()
		line = line.replace(line,line+"\""+sys.argv[1]+"\""+";")
	print line,
