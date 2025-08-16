from setuptools import find_packages, setup
from typing import List

# Function to read requirements.txt and return a list of packages
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newlines and spaces
        requirements = [req.strip() for req in requirements if req.strip()]
        # Remove editable installs if present
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="ML_PROJECT",                        # Project name
    version="0.0.1",                          # Version
    author="Krishna",                         # Your name
    author_email="krishna03@gmail.com",       # Your email
    packages=find_packages(),                 # Auto-detect packages
    install_requires=get_requirements("requirements.txt"),  # Dependencies
    python_requires=">=3.8",                  # Minimum Python version
    include_package_data=True,                # Include non-code files (like data)
    description="A Machine Learning project",# Short description
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
