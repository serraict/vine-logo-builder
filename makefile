VENV_DIR = venv
INPUT_DIR = input
OUTPUT_DIR = output
SCRIPT = main.py

# Targets
.PHONY: all venv install_deps clean create_output_dir process_logos

# Create a virtual environment
bootstrap:
	python -m venv $(VENV_DIR)
	@echo "Created virtual environment in $(VENV_DIR), activate it with 'source $(VENV_DIR)/bin/activate'"

# Install dependencies in the virtual environment
update:
	pip install -r requirements.txt

# Create the output directory if it doesn't exist
create_output_dir:
	mkdir -p $(OUTPUT_DIR)

# Process logos and overlay icons
process_logos: create_output_dir
	python $(SCRIPT)

# Clean up the environment and output
clean:
	rm -rf $(OUTPUT_DIR)