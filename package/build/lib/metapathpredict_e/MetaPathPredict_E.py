"""
Command Line Interface for MetaPathPredict-E:
====================================

.. currentmodule:: metapathpredict_e

class methods:
   MetaPathPredict-E methods
"""


import logging
import argparse
import datetime
import pickle
import os
import sys
import re
import math
import importlib
from typing import Iterable, List, Dict, Set, Optional, Sequence
from itertools import chain

# disable tensorflow info messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import sklearn
import numpy as np
import pandas as pd
import keras
#from torchvision import transforms
#import torch.optim as optim
#from torch.utils.data import Dataset, DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.metrics import classification_report
#import torch
#import torch.nn as nn

import warnings
from sklearn.exceptions import InconsistentVersionWarning
warnings.filterwarnings(action='ignore', category=InconsistentVersionWarning)

from metapathpredict_e.utils import InputData
from metapathpredict_e.utils import AnnotationList


class Models:

    """Platform-agnostic command line functions available in MetaPathPredict-E."""
 
 
    @classmethod
    def predict_eukaryote(cls, args: Iterable[str] = None) -> int:
        """Predict the presence or absence of select KEGG modules on eukaryotic
        annotation data.

        Parameters
        ----------
        args : Iterable[str], optional
            value of None, when passed to `parser.parse_args` causes the parser to
            read `sys.argv`

        Returns
        -------
        return_call : 0
            return call if the program completes successfully

        """
        
        # disable tensorflow info messages
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

        parser = argparse.ArgumentParser()

        parser.add_argument(
            "--input",
            "-i",
            action = "extend",
            nargs = "+",
            dest="input",
            required=True,
            help="input file path(s) and name(s) [required]",
        )
        parser.add_argument(
            "--annotation-format",
            "-a",
            dest="annotation_format",
            required=True,
            help="annotation format (kofamscan, kofamscan-web, dram, or koala) [default: kofamscan]",
        )
        parser.add_argument(
            "--kegg-modules",
            "-k",
            dest="kegg_modules",
            required=False,
            default=None,
            action="extend",
            nargs="+",
            help="KEGG modules to predict [default: MetaPathPredict-E KEGG modules]",
        )
        parser.add_argument(
            "--output",
            "-o",
            dest="output",
            required=True,
            help="output file path and name [required]",
        )
        parser.add_argument(
            "--group",
            "-g",
            dest="group",
            required=True,
            help="eukaryotic group; one of fungi, streptophyta, chlorophyta, alveolata, rhizaria, stramenopiles, excavata, metazoa, or general [required]",
        )
        
        # parse command line arguments
        args = parser.parse_args()
        
        # find path to MetaPathPredict-E
        module_dir = importlib.resources.files('metapathpredict_e')
        
        # get the path to the data files
        data_dir = module_dir.joinpath("data/")
        
        # create dictionary of  paths to all the eukaryotic scaler files
        scaler_dict = {}
        scaler_dict["fungi"] = module_dir.joinpath("data/euk_common_scaler_fungi_030324.pkl")
        scaler_dict["streptophyta"] = module_dir.joinpath("data/euk_common_scaler_streptophyta_030324.pkl")
        scaler_dict["chlorophyta"] = module_dir.joinpath("data/euk_common_scaler_chlorophyta_030324.pkl")
        scaler_dict["alveolata"] = module_dir.joinpath("data/euk_common_scaler_alveolata_030324.pkl")
        scaler_dict["rhizaria"] = module_dir.joinpath("data/euk_common_scaler_rhizaria_030324.pkl")
        scaler_dict["stramenopiles"] = module_dir.joinpath("data/euk_common_scaler_stramenopiles_030324.pkl")
        scaler_dict["excavata"] = module_dir.joinpath("data/euk_common_scaler_excavata_030324.pkl")
        scaler_dict["metazoa"] = module_dir.joinpath("data/euk_common_scaler_metazoa_030324.pkl")
        scaler_dict["general"] = module_dir.joinpath("data/euk_common_scaler_allData_032724.pkl")


        # create dictionary of paths to all the eukaryotic model files
        model_dict = {}
        model_dict["fungi"] = module_dir.joinpath("data/fungi_costSensitive_030324.keras")
        model_dict["streptophyta"] = module_dir.joinpath("data/streptophyta_costSensitive_030324.keras")
        model_dict["chlorophyta"] = module_dir.joinpath("data/chlorophyta_costSensitive_030324.keras")
        model_dict["alveolata"] = module_dir.joinpath("data/alveolata_costSensitive_030324.keras")
        model_dict["rhizaria"] = module_dir.joinpath("data/rhizaria_costSensitive_030324.keras")
        model_dict["stramenopiles"] = module_dir.joinpath("data/stramenopiles_costSensitive_030324.keras")
        model_dict["excavata"] = module_dir.joinpath("data/excavata_costSensitive_030324.keras")
        model_dict["metazoa"] = module_dir.joinpath("data/metazoa_costSensitive_030324.keras")
        model_dict["general"] = module_dir.joinpath("data/allData_costSensitive_032724.keras")
 
        # get the paths to eukaryotic labels data, and required columns for predictions
        #eukaryotic_labels_path = module_dir.joinpath("data/eukaryotic_labels.pkl")
        #eukaryotic_requiredCols_path = module_dir.joinpath("data/eukaryotic_requiredCols.pkl")
        
        
        # create dictionary of paths to all the eukaryotic label files
        label_dict = {}
        label_dict["fungi"] = module_dir.joinpath("data/fungi_module_names_062224.pkl")
        label_dict["streptophyta"] = module_dir.joinpath("data/streptophyta_module_names_062224.pkl")
        label_dict["chlorophyta"] = module_dir.joinpath("data/chlorophyta_module_names_062224.pkl")
        label_dict["alveolata"] = module_dir.joinpath("data/alveolata_module_names_062224.pkl")
        label_dict["rhizaria"] = module_dir.joinpath("data/rhizaria_module_names_062224.pkl")
        label_dict["stramenopiles"] = module_dir.joinpath("data/stramenopiles_module_names_062224.pkl")
        label_dict["excavata"] = module_dir.joinpath("data/excavata_module_names_062224.pkl")
        label_dict["metazoa"] = module_dir.joinpath("data/metazoa_module_names_062224.pkl")
        label_dict["general"] = module_dir.joinpath("data/general_module_names_062224.pkl")
        

        # set the scaler file path
        scaler_path = scaler_dict[args.group]
        
        # set the model file path
        model_path = model_dict[args.group]
        
        # set the model file path
        labels_path = label_dict[args.group]


        # load the scaler
        with open(scaler_path, "rb") as f:
          model_scaler = pickle.load(f)
        
        # load the label data
        with open(labels_path, "rb") as f:
          labels = pickle.load(f)
          
        # # load the required columns data
        # with open(requiredCols_path, "rb") as f:
        #   requiredCols = pickle.load(f)

        # load the model
        #models = [keras.models.load_model(model_0_path), keras.models.load_model(model_1_path)]
        model = keras.models.load_model(model_path)

        # load the input features
        files_list = InputData(files = args.input) 
        
        if args.annotation_format == "kofamscan":
          files_list.read_kofamscan_detailed_tsv()
          
        elif args.annotation_format == "kofamkoala":
          files_list.read_kofamkoala()
          
        elif args.annotation_format == "dram":
          files_list.read_dram_annotation_tsv()
          
        elif args.annotation_format == "koala":
          files_list.read_koala_tsv()
        
        else:
          logging.error("""Did not recognize annotation format; use "kofamscan", "kofamkoala", "dram", or "koala""""")
          sys.exit(0)
          
        logging.info(f"Reading input files with format: {args.annotation_format}")
          
        # model_0_cols = np.ndarray.tolist(model_0_scaler.feature_names_in_)
        # model_1_cols = np.ndarray.tolist(model_1_scaler.feature_names_in_)
        # reqColsAll = list(set(model_0_cols).union(set(model_1_cols)))

        # reqColsAll = requiredCols
        
        input_features = AnnotationList(
          requiredColumnsAll = model_scaler.feature_names_in_, # add list of all required columns for model #1 and model #2
          requiredColumnsModel = model_scaler.feature_names_in_, # add list of all required columns for model
          annotations = files_list.annotations)

        input_features.create_feature_df()
        input_features.check_feature_columns()
        # input_features.select_model_features()
        # input_features.transform_model_features(model_0_scaler, model_1_scaler)

        logging.info("Making KEGG module presence/absence predictions")

        predictions_list = []
        #for prediction_iteration in range(1):
          

        # predict
        logging.info(f"Model for {args.group} is making predictions")
        predictions = model.predict(input_features.feature_df)

        # round predictions
        roundedPreds = np.round(predictions)
          
        predsDf = pd.DataFrame(data = roundedPreds, columns = labels).astype(int)

        predictions_list.append(predsDf)
          
        logging.info(f"Model for {args.group} completed making predictions")
          
        logging.info("All done.")

        out_df = pd.concat(predictions_list, axis = 1)

        if args.kegg_modules is not None:
          if all(modules in out_df.columns for modules in args.kegg_modules):
            out_df = out_df[args.kegg_modules]
          else:
            logging.error("""Did not recognize one or more KEGG modules specified with --kegg-modules; keeping all prediction columns""")

        out_df.insert(loc = 0, column = 'file', value = args.input)
        
        logging.info(f"Writing output to file: {args.output}")
        out_df.to_csv(args.output, sep='\t', index=None)

        #logging.info(f"Output matrix size: {out_df.shape[0]} x {out_df.shape[1]}")
