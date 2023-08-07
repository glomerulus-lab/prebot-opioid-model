## gnap_mod_sim/
- **gnap_output_plots/** - various figures outputted from each $g_{NaP}$ modulation simulation
- **gnap_synblock_output_plots/** - various figures outputted from each $g_{NaP}$ modulation simulation with synaptic block
- **gnap_burst_analysis.ipynb** - notebook for analyzing burst statistics
- **explore_network.ipynb** - notebook for exploratory analysis and regression of period, amplitude, width mean and irregularity of every network in each phase of the experiment against the count of excitation and inhibition
- **get_burst_stats.py** - postprocessing script that reads every .pkl file and outputs a .csv file containing burst statistics 
- **burst_stats** - dataset of burst statistics for network seeds 1-40 with G_NaP decreasing by 10%, 30%, and 50% (to be used in burst_analysis.ipynb)
- **gnap_mod_tbq_counts.csv** - dataset containing number of T/B/Q neurons in each condition
- **quickstart.ipynb** - notebook for stepping through the experiment code (run_gnap_mod.py), useful for debugging
- **run_gnap_mod.py** - code for running the experiment, outputs traces and saves data into .pkl files
- **run_gnap_synblock.py** - run the network in a specified experimental condition, with synapses blocked
- **gnap_count_tbq.py** - script for counting tonic, bursting, and quiescent neurons in each network, outputs into gnap_mod_tbq_counts.csv

### Running the experiment
run_damgo_ramp.py arguments:
- ```prefix```: the name of the run, which is used for data/figure saving purposes. (This is always the first argument)
- ```run_seed```: network seed to be simulated
- ```g_nap_str```: The amount to increase or decrease $g_{NaP}$ by (e.g. pass in 0.3 for a 30% increase, -0.3 for a 30% decrease)
- ```hyp_opioid```: the opioid dosage given when DAMGO is turned on (pA), default value is 4 pA
- ```syn_shut```: the maximum decrease in synaptic strength [0,1] when DAMGO is turned on, default value is 0.5 (meaning that synaptic strength decreases by half)

run_gnap_synblock.py arguments are the same as above, but also with:
- ```struct```: choose 'clouds' (which refers to the two-cloud population of the network in gNaP/gLeak space) or 'grid' to generate neurons across a grid of gNaP and gLeak values (for computing phase boundaries)
- ```condition```: choose 'Control', 'DAMGO', 'G_NaP', or 'DAMGO+G_NaP'

#### Example invocations:
```bash
# increasing G_NaP by 30%
python run_gnap_mod.py seed1-gnap-03 --run_seed 1 --g_nap_str 0.3

# decreasing G_NaP by 30% (note: this effect is clearer when the opioid and synaptic shutdown isn't as strong)
python run_gnap_mod.py seed1-gnap-03 --run_seed 1 --g_nap_str -0.3 --hyp_opioid 3 --syn_shut 0.3

# run synaptic block on network seed 1 when DAMGO and the g_NaP + 30% perturbation are both on
python run_gnap_synblock.py seed1-gnap_synblock-03 --run_seed 1 --g_nap_str 0.3 --struct clouds --condition DAMGO+G_NaP

# run synaptic block on a grid of neurons to get the phase boundaries during control
python run_gnap_synblock.py seed1-gnap_synblock-03 --run_seed 1 --g_nap_str 0.3 --struct clouds --condition Control

# run synaptic block on a grid of neurons to get the phase boundaries during control
python run_gnap_synblock.py seed1-gnap_synblock-03 --run_seed 1 --g_nap_str 0.3 --struct clouds --condition DAMGO
```

```bash
# generating the burst statistics and count number of tonic, bursting, and quiescent neurons in every network sim
python get_burst_stats.py 1 40
python gnap_count_tbq.py
```

Run the run_synblock_clouds.sh script to account for different experimental conditions under synaptic block. Also use the run_synblock_grids.sh script to simulate neurons across a grid in the gNaP and gLeak parameter space, which we will use to generate phase boundaries later. Then execute run_gnap_mods.sh in order to simulate the gNaP modulation experiment on many different network seeds. Once the .pkl data has been generated, the script will run get_burst_stats.py and gnap_count_tbq.py to generate burst statistics and count tonic, bursting, and quiescent neurons in each network.