import argparse
import os
from icgconnect import xml_audit

def main():

    # Parsing the command line arguments
    parser = argparse.ArgumentParser(description='Combine all XMLs for a specific EGA accession')
    parser.add_argument('-i', '--input      ',  dest='input', help="Input github repository containing the XML files", required=True)
    parser.add_argument('-p', '--project_name', dest="project_name", help="Name of the ICGC project")
    parser.add_argument('-d', '--dataset    ',  dest='dataset', help="Dataset EGA accesion ID", required=True)
    parser.add_argument('-e', '--experiment ',  dest='experiment', help="Experiment EGA accession ID")
    parser.add_argument('-a', '--analysis   ',  dest='analysis', help="Analysis EGA accession ID")
    parser.add_argument('-r', '--run        ',  dest="run", help="Run EGA accession ID")
    parser.add_argument('-sa', '--sample    ',  dest="sample", help="Sample EGA accession ID")
    parser.add_argument('-st', '--study     ',  dest="study", help="Study EGA accession ID")
    parser.add_argument('-o', '--output     ',  dest='output', help="Output .xml file", required=True)
    parser.add_argument('--include-dataset', dest='include_dataset', default=False, help="Include the dataset xml", action='store_true')
    results = parser.parse_args()


    # Store the input folder and input file path
    input_folder = results.input
    output_file = results.output

    # Check if the input dataset xml file exists
    if results.include_dataset and not results.dataset=='':
        if not xml_audit.dataset_exists(input_folder, results.project_name, results.dataset):
            raise ValueError("Dataset xml does not exist:"+ results.dataset)

    # Check if the experiment xml file exists
    if not results.experiment == None and not results.experiment=='':
        if not xml_audit.experiment_exists(input_folder, results.project_name, results.dataset, results.experiment):
            raise ValueError("Experiment xml does not exist:"+ results.experiment)

    # Check if the analysis xml file exists
    if not results.analysis == None and not results.analysis=='':
        if not xml_audit.analysis_exists(input_folder, results.project_name, results.dataset, results.analysis):
            raise ValueError("Experiment xml does not exist:"+ results.analysis)

    # Check if the run xml file exists
    if not results.run == None and not results.run=='':
        if not xml_audit.run_exists(input_folder, results.project_name, results.dataset, results.run):
            raise ValueError("Run xml does not exist:"+ results.run)

    # Check if the sample xml file exists
    if not results.sample == None and not results.sample=='':
        if not xml_audit.sample_exists(input_folder, results.project_name, results.dataset, results.sample):
            raise ValueError("Sample xml does not exist:"+ results.run)

    # Check if the study xml file exists
    if not results.study == None and not results.study=='':
        if not xml_audit.study_exists(input_folder, results.project_name, results.dataset, results.study):
            raise ValueError("Study xml does not exist:"+ results.study)

    # Generating the combined xml files
    xml_audit.quick_generate(input_folder, results.project_name,output_file, results.dataset, results.sample, results.study, results.run, results.experiment, results.analysis,results.include_dataset)

def validate_file_path(file_path):
    if not os.path.isfile(file_path):
        raise ValueError(file_path+" does not exist")
    return  True


if __name__ == "__main__":
    main()
