from setuptools import Extension, setup, find_packages
import os

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Natural Language :: English",
    "License :: OSI Approved :: BSD License",
    "Operating System :: Linux, MacOS, Windows",
    "Programming Language :: Python :: 3.10.6+"
]

setup(
    name="metapathpredict_e", 
    description="Tool for predicting the presence or absence of KEGG modules in eukaryotic genomes",
    author="D. Geller-McGrath",
    author_email="dgellermcgrath@gmail.com",
    package_dir={"": "src"},
    packages=["metapathpredict_e"],
    package_data={"metapathpredict_e": ["data/*.*"]},
    install_requires=[
      "scikit-learn>=1.1.3",
      "tensorflow>=2.10.0",
      "numpy>=1.23.4",
      "pandas>=1.5.2",
      "keras>=2.10.0",
    ],
    entry_points={
        "console_scripts": [
            #"MetaPathTrain = metapathpredict.MetaPathPredict:Models.train", 
            "MetaPathPredict_E = metapathpredict_e.MetaPathPredict_E:Models.predict_eukaryote", 
            #"MetaPathModules = metapathpredict.MetaPathPredict:Models.show_available_modules",
            #"DownloadModels = metapathpredict_e.download_models:Download.download_models",
        ]
    },
    classifiers=CLASSIFIERS,
    include_package_data=True,
    #ext_modules=cythonize("src/metapathpredict/cpp_mods.pyx")
 )
