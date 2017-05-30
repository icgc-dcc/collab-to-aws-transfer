import requests
import json
import subprocess
import os
import csv
import hashlib
from pkg_resources import resource_string
from shutil import copyfile
import argparse

#accessToken=<access token>

_COLLAB_URL = "https://meta.icgc.org"
#icgconnect/utils


#import pysam
def main():
    parser = argparse.ArgumentParser(description='Download files from collab')
	parser.add_argument('-p', '--project_name', dest="project_name", help="Name of the ICGC project", required=True)
	parser.add_argument('-f', '--file_name', dest="file_name", help="EGA file name", required=True)
	parser.add_argument('-o', '--output', dest='output', help="Output file name", required=True)

    results = parser.parse_args()

    file_list = randomword(60)+".txt"

    try:
        try:
            os.environ['ASCP_EGA_HOST']
    # Check if ASCP_EGA_USER environment variable exists: ega username
			os.environ['ASCP_EGA_USER']

			# Check if ASPERA_SCP_PASS environment variable exists: ascpera password
			os.environ['ASPERA_SCP_PASS']
		except KeyError:
			raise KeyError("Global Variable: ASCP_EGA_HOST, ASCP_EGA_USER and ASPERA_SCP_PASS must exist in the environment.")

		# Raise an error if the output file exists
		if os.path.isfile(results.output):
			raise ValueError("Output file already exists")

		# Write the file to be downloaded to the temporary file
		with open(file_list, 'w') as f:
			f.write(os.path.join('data',results.project_name,results.file_name))
			f.write('\n')

		# Download process
		subprocess.call(['ascp','-k','1','-QTl','100m','--file-list='+file_list,'--partial-file-suffix=PART','--ignore-host-key','--mode=recv','--host='+os.environ['ASCP_EGA_HOST'],'--user='+os.environ['ASCP_EGA_USER'],'.'])

		os.rename(results.file_name, results.output)

		# Deletion of temporary elements
		os.remove(file_list)
	except Exception, err:
		print str(err)
		if os.path.isfile(file_list):
			os.remove(file_list)
		exit(1)



def randomword(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

 if __name__ == "__main__":
    main()
