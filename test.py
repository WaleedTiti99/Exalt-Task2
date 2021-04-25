import json
import os
import logging

f = open('CVM_RPM_LIST_MANIFEST.json',)

data = json.load(f)

for i in range (len(data['CESA_list'])):
	rpm_name = data['CESA_list'][i]['RPM_list'][0]['name']
	rpm_pkg = data['CESA_list'][i]['RPM_list'][0]['rpm_pkg']
	os.system('yum -y install '+rpm_name)
	os.system('wget -P /home/waleed/Desktop/PythonCourse/Task/complete_task https://linuxsoft.cern.ch/cern/centos/7/updates/x86_64/Packages/'+rpm_pkg)
	logging.basicConfig(level = logging.INFO,
						format = '%(asctime)s %(filename)s %(message)s',
						datefmt = '%d/%m/%Y %I:%M:%S %p',
						filename = 'log_info.log',
						filemode='a')
	logging.info("Downloaded package: "+rpm_name)

os.system("tar -cf CVM_PE_GI-7.7r1.6.1-20200303-x86_64.tar complete_task/")
os.system("gzip CVM_PE_GI-7.7r1.6.1-20200303-x86_64.tar")


