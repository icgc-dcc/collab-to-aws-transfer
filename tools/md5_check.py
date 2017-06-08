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
      file_md5sum:
        type: string
"""
file_ = task_dict.get('input').get('file')
file_md5sum = task_dict.get('input').get('file_md5sum')

task_start = int(time.time())

if file_md5sum != str(get_md5(file_)):
    with open('jt.log', 'w') as f: f.write(str("md5sum of file does not match given md5"))
    sys.exit(1)  # task failed

task_stop = int(time.time())
