#!/usr/bin/env python

import os
import sys
import time
import subprocess
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])
cwd = os.getcwd()


file_name = task_dict.get('input').get('file_name')
object_id = task_dict.get('input').get('object_id')
file_md5sum = task_dict.get('input').get('file_md5sum')
idx_file_name = task_dict.get('input').get('idx_file_name')
idx_object_id = task_dict.get('input').get('idx_object_id')

task_start = int(time.time())

try:
    print subprocess.check_output(['icgc-storage-client','--profile',' collab','download','--object-id', object_id,'--output-dir', cwd, '--force' ])

except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
    sys.exit(1)  # task failed

if idx_object_id:
    try:
        print subprocess.check_output(['icgc-storage-client','--profile',' collab','download','--object-id', idx_object_id,'--output-dir', cwd, '--force' ])

    except Exception, e:
        with open('jt.log', 'w') as f: f.write(str(e))
        sys.exit(1)  # task failed

task_stop = int(time.time())

idx_file_ = None
if idx_file_name:
    idx_file_ = os.path.join(cwd, idx_file_name)

output_json = {
    'file': os.path.join(cwd, file_name),
    'file_name': file_name,  # we may need to deal with encrypted / unencypted file names
    'object_id': object_id,
    'file_md5sum': file_md5sum,
    'idx_file': idx_file_,
    'idx_file_name': idx_file_name,  # we may need to deal with encrypted / unencypted file names
    'idx_object_id': idx_object_id,
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
