#!/usr/bin/env python

import os
import sys
import time
import subprocess
from utils import get_md5
from utils import get_task_dict, save_output_json

task_dict = get_task_dict(sys.argv[1])
#task_dict = get_task_dict("""{"input": {"file": "/home/ubuntu/collab-to-aws-transfer-jt/tools/c9dc3c3fed697c072a3b00c9fe2c4490.CPCG_0047_Ly_R_PE_294_WG_111216_h801_0065_AD0813ACXX_6_NoIndex_R2.fastq.gz","collab_file_id": "EGAF00000588185","file_name": "c9dc3c3fed697c072a3b00c9fe2c4490.CPCG_0047_Ly_R_PE_294_WG_111216_h801_0065_AD0813ACXX_6_NoIndex_R2.fastq.gz","file_md5sum": "c9dc3c3fed697c072a3b00c9fe2c4490","object_id": "7e2d1747-cda9-5843-8103-d6192cd55af4"}}""")
cwd = os.getcwd()

"""
    input:
      file:
        type: string
      file_name:
        type: string
      file_md5sum:
        type: string
      object_id:
        type: string
      bundle_id: bundle_id
        type: string
      file_size:
        type: string
"""
file_ = task_dict.get('input').get('file')
file_name = task_dict.get('input').get('file_name')
file_md5sum = task_dict.get('input').get('file_md5sum')
object_id = task_dict.get('input').get('object_id')
#project_code = task_dict.get('input').get('project_code')

if file_md5sum is None:
    file_md5sum = str(get_md5(file_))

task_start = int(time.time())

try:
    print(file_md5sum)
    print subprocess.check_output(['icgc-storage-client','upload','--file', file_, '--object-id', object_id, '--md5', file_md5sum])
    #icgc-storage-client upload --file test --object-id fbd35588-5bf8-560c-873a-0410f49e5748 --md5 d8e8fca2dc0f896fd7cb4cb0031ba249 --force
except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))

    raise Exception  #for testing
    sys.exit(1)  # task failed

# try:
#     r = subprocess.check_output(['curl','https://raw.githubusercontent.com/jt-hub/ega-collab-transfer-tools/master/download_ega_file.py','|','python','-','-p',project_code,'-f', ega_file_id+".aes", '-o', file_name])
# except Exception, e:
#     print e
#     sys.exit(1)  # task failed


# complete the task

task_stop = int(time.time())


output_json = {
    'file_md5sum': file_md5sum,
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
