#!/usr/bin/env python

import os
import sys
import time
import subprocess
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])
cwd = os.getcwd()

"""
    input:
      project_code:
        type: string
      ega_file_id:
        type: string
      file_name:
        type: string
      file_md5sum:
        type: string
      object_id:
        type: string
"""

file_name = task_dict.get('input').get('file_name')
object_id = task_dict.get('input').get('object_id')
file_md5sum = task_dict.get('input').get('xml_file_md5sum')


task_start = int(time.time())

try:
    print subprocess.check_output(['icgc-storage-client','--profile',' collab','download','--object-id', object_id,'--output-dir', cwd ])

except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
    print(e)
    raise Exception
    sys.exit(1)  # task failed

task_stop = int(time.time())

"""
    output:
      file:  # new field
        type: string
        is_file: true
      file_name:  # passing through
        type: string
      file_md5sum:  # passing through
        type: string
      object_id:  # passing through
        type: string
"""

output_json = {
    'file': os.path.join(cwd, file_name),
    'file_name': file_name,  # we may need to deal with encrypted / unencypted file names
    'object_id': object_id,
    'file_md5sum': file_md5sum,
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
