import requests
import json
import subprocess
import os
import csv
import hashlib
from pkg_resources import resource_string

accessToken=<access token>

_COLLAB_URL = "https://meta.icgc.org"

def login(email, password):
	""" Login to collab
		Args:
			email (str): 		Email of the user to login
			password (str): 	Password of the user
		Returns:
			str: The return value. A session token
		Raises:
			ValueError: If `email` format is not a valid email
			ValueError: If credentials ar invalid
	"""

	# Email must be a valid email
	if not re.match("[^@]+@[^@]+\.[^@]+", email):
		raise ValueError(email+" is not a valid email")

	try:
		return _result_from_response(requests.get(_api_access_endpoint("/users/"+email+"?pass="+password, None), verify=False))[1]
	except ValueError, err:
		raise ValueError("EGA response: "+str(err)+" - Verify email and password")







#icgconnect/utils

import hashlib
import os
from shutil import copyfile
#import pysam

def get_file_md5(fname):
	if not os.path.isfile(fname):
		raise ValueError("The file does not exist: "+fname)
	hash_md5 = hashlib.md5()
	with open(fname, "rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def get_file_size(fname):
	if not os.path.isfile(fname):
		raise ValueError("The file does not exist: "+fname)
	return os.path.getsize(fname)

def delete_file(filename):
	""" Delete a file in the local system
		Args:
			filename (str):	Path of the file name
		Raises:
			ValueError:	The file does not exist
	"""
	if not os.path.isfile(filename):
		raise ValueError("The file does not exist: "+ filename)
	os.remove(filename)

def generate_bai_from_bam(bam_file_path, file_output):
	""" Generate a bai file from a bam file
		Args:
			bam_file_path (str):	Path of the bam file
			file_output (str):		Path to create the bai file
		Raises:
			ValueError:	Bam file does not exist
			ValueError: Output file already exists
			ValueError: Input same as output file
	"""
	if not os.path.isfile(bam_file_path):
		raise ValueError("Bam file does not exist: "+bam_file_path)

	if os.path.isfile(file_output):
		raise ValueError("The output file already exists: "+file_output)

	if bam_file_path == file_output:
		raise ValueError("The input file cannot be the same as the output file: "+bam_file_path)

	pysam.index(bam_file_path)
	if not bam_file_path+".bai" == file_output:
		copyfile(bam_file_path+".bai",file_output)
