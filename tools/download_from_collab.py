import requests
import json
import subprocess
import os
import csv
import hashlib
from utils import file_utils
from pkg_resources import resource_string

_COLLAB_URL = "https://meta.icgc.org"

def download(icgc_storage_client, force):
    raise Exception
    """ download files listed in a manifest file to Collaboratory
        Args:
            manifest_file (str):    The local path of a manifest file
    """
    #_validate_manifest_file(manifest_file)
    try:
        if force == True:
            subprocess.check_output([icgc_storage_client,'--profile','collab','download','--object_id', object_id,'--force'])
            print('force')
        else:
            print('notforce')
            subprocess.check_output([icgc_storage_client,'--profile','collab','download','--object_id', object_id])
    except subprocess.CalledProcessError as err:
        raise Exception("download to collab failed: "+str(err))
