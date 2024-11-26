import argparse
import os
from roboflow import Roboflow

# Function to download dataset with specified arguments
def download_dataset(workspace_name, project_name, version_number, model_name, dataset_name):

    api_key = "cmZgR1PSSNwyxDMkeJrI"
    datasets_path = '/Users/jjookim/Projects/AIForce/datasets'

    # Initialize Roboflow with the API key
    rf = Roboflow(api_key=api_key)

    # Fetch the workspace, project, and version
    workspace = rf.workspace(workspace_name)
    project = workspace.project(project_name)
    version = project.version(version_number)

    # Download the dataset using the chosen model (e.g., yolov11, yolov5, etc.)
    version.download(model_name, location=os.path.join(datasets_path, dataset_name))

    print(f"Dataset for model '{model_name}' downloaded successfully.")


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Download dataset from Roboflow.")

    # Define the long-form arguments that the script accepts
    parser.add_argument("--workspace_name", type=str, required=True, help="The name of the workspace in Roboflow.")
    parser.add_argument("--project_name", type=str, required=True, help="The project name in the Roboflow workspace.")
    parser.add_argument("--version_number", type=int, required=True, help="The version number of the dataset.")
    parser.add_argument("--dataset_name", type=str, required=True, help="The name you want to give to the downloaded dataset folder.")
    parser.add_argument("--model_name", type=str, required=True, help="The model format you want to download (e.g., yolov11, yolov5).")
    # Parse the arguments
    args = parser.parse_args()

    # Call the download function with the parsed arguments
    download_dataset(args.workspace_name, args.project_name, args.version_number,args.model_name, args.dataset_name)



'''
python download_dataset.py \
  --workspace_name "aiforce" \
  --project_name "final-nzzto" \
  --version_number 5 \
  --model_name "yolov8" \
  --dataset_name "final_dataset"
'''