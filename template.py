import os
from pathlib import Path

project_name = "SafeGaurd"

list_of_files = [
    "Data/.gitkeep",
    "Docs/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/Components/__init__.py",
    f"{project_name}/Components/Data_Ingestion.py",
    f"{project_name}/Components/Data_Validation.py",
    f"{project_name}/Components/Model_Trainer.py",
    f"{project_name}/Components/model_Pusher.py",
    f"{project_name}/Configuration/__init__.py",
    f"{project_name}/Configuration/S3_Operations.py",
    f"{project_name}/Constant/__init__.py",
    f"{project_name}/Constant/Training_Pipeline/__init__.py",
    f"{project_name}/Constant/Application.py",
    f"{project_name}/Entity/__init__.py",
    f"{project_name}/Entity/Artifacts_Entity.py",
    f"{project_name}/Entity/Config_Entity.py",
    f"{project_name}/Exception/__init__.py",
    f"{project_name}/Logger/__init__.py",
    f"{project_name}/Pipeline/__init__.py",
    f"{project_name}/Pipeline/Training_Pipeline.py",
    f"{project_name}/Utils/__init__.py",
    f"{project_name}/Utils/Main_Utils.py",
    "templates/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)

    
    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass