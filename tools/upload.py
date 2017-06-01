import os
import sys
import time
import subprocess

from utils import get_task_dict, save_output_json

#task_dict = get_task_dict(sys.argv[1])
task_dict = get_task_dict("""{"input": {"project_code": "23423","collab_file_id": "2341","file_name": "data/test","file_md5sum": "sdfs","object_id": "fbd35588-5bf8-560c-873a-0410f49e5748"}}""")
cwd = os.getcwd()

"""
    input:
      project_code:
        type: string
      collab_file_id:
        type: string
      file_name:
        type: string
      file_md5sum:
        type: string
      object_id:
        type: string
"""
collab_file_id = task_dict.get('input').get('collab_file_id')
file_name = task_dict.get('input').get('file_name')
file_md5sum = task_dict.get('input').get('file_md5sum')
object_id = task_dict.get('input').get('object_id')
project_code = task_dict.get('input').get('project_code')


task_start = int(time.time())

try:
    print subprocess.check_output(['icgc-storage-client','upload','--file', file_name, '--object-id', 'fbd35588-5bf8-560c-873a-0410f49e5748', '--md5', '039d75310a642d7ee2d2d8dfd7107c31'])

except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))

    #raise Exception  #for testing
    sys.exit(1)  # task failed

# try:
#     r = subprocess.check_output(['curl','https://raw.githubusercontent.com/jt-hub/ega-collab-transfer-tools/master/download_ega_file.py','|','python','-','-p',project_code,'-f', ega_file_id+".aes", '-o', file_name])
# except Exception, e:
#     print e
#     sys.exit(1)  # task failed


# complete the task

task_stop = int(time.time())

"""
    output:
      file:  # new field
        type: string
        is_file: true
      collab_file_id:  # passing through
        type: string
      file_name:  # passing through
        type: string
      file_md5sum:  # passing through
        type: string
      object_id:  # passing through
        type: string
"""

output_json = {
    'file': os.path.join(cwd, file_name),
    'collab_file_id': collab_file_id,
    'file_name': file_name,  # we may need to deal with encrypted / unencypted file names
    'object_id': object_id,
    'file_md5sum': file_md5sum,
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
