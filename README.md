# Modeling of opioids in the Pre-Bötzinger complex

This repository uses the [Brian 2](https://brian2.readthedocs.io/en/stable/) neural simulator (Python) to run simulations perturbing Pre-Bötzinger complex neuronal networks and analyze the resulting data. Published as:

GM Chou, NE Bush, RS Phillips, NA Baertsch, KD Harris. [Modeling effects of variable preBötzinger complex network topology and cellular properties on opioid-induced respiratory depression and recovery] (https://doi.org/10.1101/2023.08.29.555355). In press, eNeuro.

## Subdirectories and files
- **brian_utils/** - Utility functions to be used for postprocessing and analysis
- **data/** - .pkl files of each experiment, which contain population monitors and spike monitors (refer to Brian docs). Note: these files are not on GitHub due to storage constraints.
- **simulations/** - Subdirectories for each type of simulation. Each contains simulation scripts, network and burst statistics, and exploratory analyses
- **figure_notebooks/** - Jupyter notebooks for generating the figures in the manuscript
- **harris_eqs_oprmv1_gnap.yaml** - Contains Hodgkin-Huxley style equations to be parsed by the experiment scripts 
- **harris_ns_oprmv1.yaml** - Contains constant parameters

### Disclaimer
- The filepaths specified in each script pertain to the WWU Computer Science Linux systems. To run our code on a different machine, you will need to modify filepaths and ensure that all the necessary packages are installed.
