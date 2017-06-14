#!/usr/bin/env python

import os
import sys
import time
from utils import get_md5, get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])

"""
    input:
      file:
        type: string
"""
file_ = task_dict.get('input').get('file')
idx_file_ = task_dict.get('input').get('idx_file')

task_start = int(time.time())

try:
	os.remove(file_)

except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
    sys.exit(1)  # task failed

if idx_file_:
    try:
        os.remove(idx_file_)
    except Exception, e:
        with open('jt.log', 'w') as f: f.write(str(e))
        sys.exit(1)  # task failed

# try:
#     r = subprocess.check_output(['curl','https://raw.githubusercontent.com/jt-hub/ega-collab-transfer-tools/master/download_ega_file.py','|','python','-','-p',project_code,'-f', ega_file_id+".aes", '-o', file_name])
# except Exception, e:
#     print e
#     sys.exit(1)  # task failed


# complete the task

task_stop = int(time.time())
