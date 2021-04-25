import json
import yaml
import logging

def write_json_file():
    with open("data.yaml",'r') as s:
        y = yaml.load(s)
        j = json.dumps(y['CVM'])
        jsonFile = open('CVM_RPM_LIST_MANIFEST.json','w')
        jsonFile.write(j)
        jsonFile.close()

def write_release_notes():
    with open("data.yaml",'r') as s:
        y = yaml.load(s)
        release = y['Release-Notes']
        releaseNotes = open('CVM_PE_GI-7.7r1.7.1-20200319-x86_64.release_notes','w')
        releaseNotes.write(release)
        releaseNotes.close()

def write_log(file_type):
    logging.basicConfig(level = logging.INFO,
                        format = '%(asctime)s %(filename)s %(message)s',
                        datefmt = '%d/%m/%Y %I:%M:%S %p',
                        filename = 'log_info.log',
                        filemode='w')
    logging.info("Created " + file_type)

write_log("YAML File")
write_json_file()
write_release_notes()
write_log("JSON File")
write_log("Release Notes File")
