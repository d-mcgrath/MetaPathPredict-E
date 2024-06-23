# MetaPathPredict-E

The MetaPathPredict-E Python module is an extension to MetaPathPredict. It is designed to predict the presence or absence of KEGG metabolic modules in eukaryotic genomes and transcriptomes recovered from environmental sequencing efforts. It contains models to make predictions for several eukaryotic groups including Fungi, Streptophyta, Chlorophyta, Excavata, Metazoa, Alveolata (excluding Apicomplexa), Rhizaria, and Stramenopiles. It also contains a general model that can be used for any of these, or microbial eukaryotes from other groups.

## Installation

To run MetaPathPredict-E, see the instructions below to download this repository and install it as a Python module. Note that steps 1-3 of the instructions can optionally be skipped if MetaPathPredict is already installed on the same machine.


### GitHub install:

NOTE: [Conda](https://docs.conda.io/en/latest/) is required for this installation.

1. Open a Terminal/Command Prompt window and run the following command to download the
GitHub repository to the desired location (note: change your current working directory first
to the desired download location, e.g., `~/Downloads` on MacOS):
`git clone https://github.com/d-mcgrath/MetaPathPredict-E.git`

    1. NOTE: You can also download the repository zip file from GitHub

2. In a Terminal/Command Prompt window, run the following commands from the parent directory the MetaPathPredict-E repository was cloned to:
```bash
conda create -n MetaPathPredict-E python=3.10.6 scikit-learn=1.3.0 tensorflow=2.10.0 numpy=1.23.4 pandas=1.5.2 keras=2.10.0 git=2.40.1
```
NOTE: You will be prompted (y/n) to confirm creating this conda environment. Now activate it:

```bash
conda activate MetaPathPredict-E
```

3. Install pyxet:
```bash
pip install pyxet
```
NOTE: Steps 1-3 can be skipped if the MetaPathPredict conda environment is used to install MetaPathPredict-E. Optionally use conda to activate the MetaPathPredict environment and start at step 4.

4. Once complete, pip install MetaPathPredict-E:
```bash
pip install MetaPathPredict-E/package
```

5. Download MetaPathPredict-E's models by running the following command:
```bash
Download_MetaPathPredictE_Models
```

Note: MetaPathPredict-E is now installed in the `MetaPathPredict-E` conda environment (or the `MetaPathPredict` environment if you choose to use that instead). Activate the conda environment prior to any use of MetaPathPredict-E.

### XetHub install:
Follow the instructions from the MetaPathPredict-E [XetHub](https://xethub.com/dgellermcgrath/MetaPathPredict-E) repository.

### pip install:
[not available yet]

<br>

## Functions

The following functions can be implemented to run MetaPathPredict-E on the command line:

- `MetaPathPredict-E` parses one or more input KEGG Ortholog gene annotation datasets (currently eukaryotic genome and transcriptome data is supported) and predicts the presence or absence of [KEGG Modules](https://www.genome.jp/kegg/module.html). This function takes as input the .tsv output files from the [KofamScan](https://github.com/takaram/kofam_scan) and [DRAM](https://github.com/WrightonLabCSU/DRAM) gene annotation tools as well as the KEGG KOALA online annotation platforms [blastKOALA](https://www.kegg.jp/blastkoala/), [ghostKOALA](https://www.kegg.jp/ghostkoala/), and [kofamKOALA](https://www.genome.jp/tools/kofamkoala/). Run any of these tools first and then use one or more of their output .tsv files as input to MetaPathPredict-E.
    - A single file or multiple space-separated files can be specified to the `--input` parameter, or use a wildcard (e.g., /results/*.tsv). Include full or relative paths to the input file(s). A sample of each annotation file format that MetaPathPredict-E can process is included in this repository in the [annotatation_examples](annotatation_examples) folder. The sample annotation files in [annotatation_examples](annotatation_examples) can optionally be used as input to test the installation.
    - The format of the gene annotation files (kofamscan, kofamkoala, dram, or koala) that is used as input must be specified with the `--annotation-format` parameter. Currently, only one input type can be specified at a time.
    - The full or relative path to the desired destination for MetaPathPredict-E's output .tsv file must be specified, as well as a name for the file. The output file path and name can be specified using the `--output` parameter. By default, MetaPathPredict-E does not create any default output directory nor does the output have a default file name.
    - To specify a specific KEGG module or modules to reconstruct and predict, include the module identifier (e.g., M00001) or identifiers as a space-separated list to the argument `--kegg-modules`.

- To view which KEGG modules MetaPathPredict-E can reconstruct and make predictions for, run the following on the command line: `MetaPathPredictE_Modules`.

<br>

## Basic usage

```
# predict method for making KEGG module presence/absence predictions on input gene annotations

usage: MetaPathPredict_E [-h] --input INPUT [INPUT ...] --annotation-format ANNOTATION_FORMAT
                         [--kegg-modules KEGG_MODULES [KEGG_MODULES ...]] --output OUTPUT --group GROUP

options:
  -h, --help            show this help message and exit
  --input INPUT [INPUT ...], -i INPUT [INPUT ...]
                        input file path(s) and name(s) [required]
  --annotation-format ANNOTATION_FORMAT, -a ANNOTATION_FORMAT
                        annotation format (kofamscan, kofamscan-web, dram, or koala) [default: kofamscan]
  --kegg-modules KEGG_MODULES [KEGG_MODULES ...], -k KEGG_MODULES [KEGG_MODULES ...]
                        KEGG modules to predict [default: MetaPathPredict-E KEGG modules]
  --output OUTPUT, -o OUTPUT
                        output file path and name [required]
  --group GROUP, -g GROUP
                        eukaryotic group; one of fungi, streptophyta, chlorophyta, alveolata, rhizaria, stramenopiles, excavata,
                        metazoa, or general [required]
```

<br>

## Examples with sample datasets

```
# One KofamScan gene annotation dataset
MetaPathPredict_E -i /path/to/kofamscan_annotations_1.tsv -a kofamscan -o /results/predictions.tsv

# Three KofamScan gene annotation datasets, with predictions for modules M00001 and M00003
MetaPathPredict_E \
-i kofamscan_annotations_1.tsv kofamscan_annotations_2.tsv kofamscan_annotations_3.tsv \
-a kofamscan \
-g fungi \
-k M00001 M00003 \
-o /results/predictions.tsv

# Multiple KofamScan datasets in a directory
MetaPathPredict_E -i annotations/*.tsv -a kofamscan -g fungi -o /results/predictions.tsv

# One DRAM gene annotation dataset
MetaPathPredict_E -i dram_annotation.tsv -a dram -g fungi -o /results/predictions.tsv

# Multiple DRAM datasets in a directory
MetaPathPredict_E -i annotations/*.tsv -a dram -g fungi -o /results/predictions.tsv
```

<br>

## Understanding the output

The output of running `MetaPathPredict-E` is a table. The first column, `file`, displays the full file name of each input gene annotation file. The remaining columns give the class predictions (module present = 1; module absent = 0) of KEGG modules. Each KEGG module occupies a single column in the table and is labelled by its module identifier. See a sample output below of four KEGG module predictions for three input annotation files:

| file                                 | M00001 | M00002 | M00003 | M00004 |
|--------------------------------------|--------|--------|--------|--------|
| /path/to/kofamscan_annotations_1.tsv | 1      | 1      | 0      | 1      |
| /path/to/kofamscan_annotations_2.tsv | 0      | 1      | 0      | 0      |
| /path/to/kofamscan_annotations_3.tsv | 1      | 0      | 0      | 0      |

<br>
