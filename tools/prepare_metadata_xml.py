import os
import sys
import json
import time
from random import randint
from utils import get_task_dict, save_output_json, get_md5
import subprocess

task_dict = get_task_dict(sys.argv[1])
cwd = os.getcwd()

"""
    input:
      collab_metadata_git_repo:
        type: string
      collab_metadata_path:
        type: string
      project_code:
        type: string
      bundle_id:  # collabR or collabZ ID
        type: string
      collab_dataset_id:
        type: string
      collab_sample_id:
        type: string
      collab_metadata_file_name:
        type: string
"""
project_code = task_dict.get('input').get('project_code')
bundle_id = task_dict.get('input').get('bundle_id')
collab_dataset_id = task_dict.get('input').get('collab_dataset_id')
collab_sample_id = task_dict.get('input').get('collab_sample_id')
collab_study_id = task_dict.get('input').get('collab_study_id')
collab_metadata_file_name = task_dict.get('input').get('collab_metadata_file_name')
collab_expriment_id = task_dict.get('input').get('collab_expriment_id')
collab_analysis_id = task_dict.get('input').get('collab_analysis_id')
collab_run_id = task_dict.get('input').get('collab_run_id', '')
output_file = task_dict.get('input').get('collab_metadata_file_name')
collab_metadata_repo = task_dict.get('input').get('collab_metadata_repo')

# do the real work here
task_start = int(time.time())

try:
    subprocess.check_output(['prepare_collab_xml_audit.py',
      '-i',collab_metadata_repo,
      '-p',project_code,
      '-o',output_file,
      '-d',collab_dataset_id,
      '-a',collab_analysis_id if collab_analysis_id else '',
      '-e',collab_expriment_id if collab_expriment_id else '',
      '-r',collab_run_id if collab_run_id else '',
      '-sa',collab_sample_id if collab_sample_id else '',
      '-st',collab_study_id if collab_study_id else ''])
    # subprocess.check_output(['curl','https://raw.githubusercontent.com/jt-hub/collab-collab-transfer-tools/master/prepare_collab_xml_audit.py','|','python','-',
    #   '-i',collab_metadata_repo,
    #   '-p',project_code,
    #   '-o',output_file,
    #   '-d',collab_dataset_id,
    #   '-e',collab_expriment_id if collab_expriment_id else '',
    #   '-r',collab_run_id if collab_run_id else '',
    #   '-sa',collab_sample_id if collab_sample_id else ''])
except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
    sys.exit(1)  # task failed

# complete the task
task_stop = int(time.time())


"""
    output:
      xml_file:
        type: string
        is_file: true
      xml_file_name:  # passing through from collab_metadata_file_name
        type: string
      xml_file_size:
        type: integer
      xml_file_md5sum:
        type: string
"""

output_json = {
    'xml_file': os.path.join(cwd, output_file),
    'xml_file_name': output_file,
    'xml_file_size': os.path.getsize(output_file),
    'xml_file_md5sum': get_md5(output_file),
    'runtime': {
        'task_start': task_start,
        'task_stop': task_stop
    }
}

save_output_json(output_json)
