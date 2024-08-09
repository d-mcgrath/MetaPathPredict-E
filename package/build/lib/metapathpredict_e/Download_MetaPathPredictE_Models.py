import pyxet
import importlib
from importlib import resources


class Download:
    """Functions to download MetaPathPredict-E's machine learning models"""
    
    @classmethod
    def download_models(cls):
      """Downloads MetaPathPredict-E's models.

      Returns:
        None

      """
      print("Downloading MetaPathPredict-E's models...")
      
      module_dir = resources.files('metapathpredict_e')
      data_dir = module_dir.joinpath("data/")
      
      model_1_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/allData_costSensitive_032724.keras"
      model_2_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/chlorophyta_costSensitive_030324.keras"
      model_3_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/fungi_costSensitive_030324.keras"
      model_4_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/alveolata_costSensitive_030324.keras"
      model_5_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/streptophyta_costSensitive_030324.keras"
      model_6_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/rhizaria_costSensitive_030324.keras"
      model_7_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/metazoa_costSensitive_030324.keras"
      model_8_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/stramenopiles_costSensitive_030324.keras"
      model_9_dl_path = "xet://dgellermcgrath/MetaPathPredict-E/main/package/src/metapathpredict_e/data/excavata_costSensitive_030324.keras"

      model_1_install_path = module_dir.joinpath("data/allData_costSensitive_032724.keras")
      model_2_install_path = module_dir.joinpath("data/chlorophyta_costSensitive_030324.keras")
      model_3_install_path = module_dir.joinpath("data/fungi_costSensitive_030324.keras")
      model_4_install_path = module_dir.joinpath("data/alveolata_costSensitive_030324.keras")
      model_5_install_path = module_dir.joinpath("data/streptophyta_costSensitive_030324.keras")
      model_6_install_path = module_dir.joinpath("data/rhizaria_costSensitive_030324.keras")
      model_7_install_path = module_dir.joinpath("data/metazoa_costSensitive_030324.keras")
      model_8_install_path = module_dir.joinpath("data/stramenopiles_costSensitive_030324.keras")
      model_9_install_path = module_dir.joinpath("data/excavata_costSensitive_030324.keras")

      fs = pyxet.XetFS()  # fsspec filesystem
      
      fs.get(model_1_dl_path, str(model_1_install_path))
      fs.get(model_2_dl_path, str(model_2_install_path))
      fs.get(model_3_dl_path, str(model_3_install_path))
      fs.get(model_4_dl_path, str(model_4_install_path))
      fs.get(model_5_dl_path, str(model_5_install_path))
      fs.get(model_6_dl_path, str(model_6_install_path))
      fs.get(model_7_dl_path, str(model_7_install_path))
      fs.get(model_8_dl_path, str(model_8_install_path))
      fs.get(model_9_dl_path, str(model_9_install_path))
      
      print("All done. Use MetaPathPredict_E -h to see how to make predictions.")
