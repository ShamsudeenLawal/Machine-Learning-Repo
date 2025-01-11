#!/bin/bash

# Description: Shell script to create a conda environment, install dependencies, and run a Streamlit app
# Usage: ./run_streamlit_app.sh

# Define variables
ENV_NAME="streamlit_env" # Name of the Conda environment
REQUIREMENTS_FILE="requirements.txt" # Path to the requirements file
APP_PATH="app.py"

# Check if Conda is installed
if ! command -v conda &> /dev/null; then
	echo "Error: Conda is not installed. Please install Conda and try again."
	exit 1
fi

# Create a Conda environment if it doesn't exist
if ! conda info --envs | grep -q "^$ENV_NAME"; then
	echo "Creating conda environment '$ENV_NAME'..."
	conda create --name "$ENV_NAME" python=3.9 -y
else
	echo "Conda environment 'ENV_NAME' already exists."
fi

# Activate the Conda environment
echo "Activating Conda environment '$ENV_NAME'..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"

# Install packages from requirements.txt
if [ -f "$REQUIREMENTS_FILE" ]; then
	echo "Installing packages from '$REQUIREMENTS_FILE'..."
	pip install -r "$REQUIREMENTS_FILE"
else
	echo "Error: Requirements file '$REQUIREMENTS_FILE' not found."
	exit 1
fi

# Check if the Streamlit app file exists
if [ -f "$APP_PATH" ]; then
	echo "Starting Streamlit app..."
	streamlit run "$APP_PATH"
else
	echo "Error: Streamlit app file '$APP_PATH' not found."
	exit 1
fi