## damgo_ramp_sim/
- **burst_stats/** - .csv files containing burst statistics
- **cell_classes/** - .npy files (numpy arrays) that tell which neurons are tonic, bursting, and quiescent
- **connectivity_csv/** - contains .csv files counting connection types, cell types, and calculating shutdown dosages in each network
- **networkx_objects/** - .pkl files that contain networkx objects describing the structure of each network (T/B/Q, inhibitory/excitatory/oprm1+, synaptic connections)
- **create_graphs.py** - code for creating networkx DiGraph (directed graph) objects for each network and saving them as .pkl files in networkx_objects/ 
- **damgo_ramp_analysis.ipynb** - notebook for analyzing results of the experiment
- **damgo_ramp_postproc.py** - postprocessing script that counts how many of each type of synapse are in each network and computes network shutdown values by taking the average DAMGO dosage across multiple firing rate thresholds
- **graph_metrics.ipynb** - notebook for analyzing the algebraic connectivity of each network and its various subpopulations, as well as the centrality of the individual neurons in each network.
- **plot_max_fr_ld50.py** - plots the max firing rate in a sliding 2 second window throughout the simulation against the corresponding DAMGO dosage. A logistic curve is then fitted onto the data, which can then be used to compute the LD50 of each network.
- **run_damgo_ramp.py** - code for running the experiment, outputs traces and saves data into .pkl files
- **run_damgo_ramps** - bash script for sweeping across many different network seeds
- **tbq_all_networks.py** - script for counting tonic, bursting, and quiescent neurons in each network, outputs into **connectivity_csv/random_gl_ctrl_damgo_tbq_counts.csv**

### Running the experiment
run_damgo_ramp.py arguments:
- ```prefix```: the name of the run, which is used for data/figure saving purposes. (This is always the first argument)
- ```run_seed```: network seed to be simulated
- ```hyp_opioid```: the maximum opioid current (pA), default value is 8 pA
- ```syn_shut```: the maximum decrease in synaptic strength [0,1], default value is 1 (meaning that synapses are completely shut down by the end of the simulation)
#### Example invocations:
```bash
# default parameters
python run_damgo_ramp.py seed1-damgo_ramp --run_seed 1  

# if we want to increase max opioid current to 10 pA and only decrease synaptic strength by half
python run_damgo_ramp.py seed1-damgo_ramp --run_seed 1 --hyp_opioid 10 --syn_shut 0.5
```
Edit/run the executable run_damgo_ramps script in order to sweep across many different network seeds and different parameters. Once the .pkl data has been generated, the script will run damgo_ramp_postproc.py, create_graphs.py, and then tbq_all_networks.py. 
```bash
# postprocessing the data for network seeds 1-40
python damgo_ramp_postproc.py 1 40 0.01 # for experiments with 1% connection probability
python create_graphs.py 1 40
python tbq_all_networks.py