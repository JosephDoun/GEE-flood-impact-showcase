#!/usr/bin/env bash

{
	if [ ! -d .venv ]
	then
		python -m venv .venv ;
	fi
} && \
	source .venv/bin/activate && \
{
	if [ -z "$(pip list | grep Joseph-Doundoulakis)" ]
	then
		pip install .;
	else
		echo Package is already installed.
	fi
}

python -m ipykernel install --user --name .venv --display-name "eo_code_sample";
jupyter notebook flood_impact_assessment.ipynb --allow-root;
jupyter-kernelspec uninstall .venv -y;

deactivate && echo "Virtual environment exited.";

# Run `jupyter-kernelspec uninstall .venv` to remove the kernel from jupyter.
