## gleak_mod_sim/
- **gleak_output_plots/** - various figures outputted from each $g_{Leak}$ modulation simulation
- **gleak_synblock_output_plots/** - various figures outputted from each $g_{Leak}$ modulation simulation with synaptic block
- **gleak_burst_analysis.ipynb** - notebook for analyzing burst statistics
- **get_gleak_burst_stats.py** - postprocessing script that reads every .pkl file and outputs a .csv file containing burst statistics 
- **burst_stats** - dataset of burst statistics for network seeds 1-40 with G_Leak decreasing by 10%, 30%, and 50% (to be used in burst_analysis.ipynb)
- **gleak_mod_tbq_counts.csv** - dataset containing number of T/B/Q neurons in each condition
- **run_gleak_mod.py** - code for running the experiment, outputs traces and saves data into .pkl files
- **run_gleak_synblock.py** - run the network in a specified experimental condition, with synapses blocked
- **gleak_count_tbq.py** - script for counting tonic, bursting, and quiescent neurons in each network, outputs into gleak_mod_tbq_counts.csv

### Running the experiment
run_damgo_ramp.py arguments:
- ```prefix```: the name of the run, which is used for data/figure saving purposes. (This is always the first argument)
- ```run_seed```: network seed to be simulated
- ```g_leak_str```: The amount to increase or decrease $g_{Leak}$ by (e.g. pass in 0.3 for a 30% increase, -0.3 for a 30% decrease)
- ```hyp_opioid```: the opioid dosage given when DAMGO is turned on (pA), default value is 4 pA
- ```syn_shut```: the maximum decrease in synaptic strength [0,1] when DAMGO is turned on, default value is 0.5 (meaning that synaptic strength decreases by half)

run_gleak_synblock.py arguments are the same as above, but also with:
- ```struct```: choose 'clouds' (which refers to the two-cloud population of the network in gNaP/gLeak space) or 'grid' to generate neurons across a grid of gNaP and gLeak values (for computing phase boundaries)
- ```condition```: choose 'Control', 'DAMGO', 'G_Leak', or 'DAMGO+G_Leak'

#### Example invocations:
```bash
# increasing G_Leak by 30%
python run_gleak_mod.py seed1-gleak-03 --run_seed 1 --g_leak_str 0.3

# decreasing G_Leak by 30% (note: this effect is clearer when the opioid and synaptic shutdown isn't as strong)
python run_gleak_mod.py seed1-gleak-03 --run_seed 1 --g_leak_str -0.3 --hyp_opioid 3 --syn_shut 0.3

# run synaptic block on network seed 1 when DAMGO and the G_Leak -30% perturbation are both on
python run_gleak_synblock.py seed1-gleak_synblock-03 --run_seed 1 --g_leak_str -0.3 --struct clouds --condition DAMGO+G_Leak

# run synaptic block on a grid of neurons to get the phase boundaries during control
python run_gleak_synblock.py seed1-gleak_synblock-03 --run_seed 1 --struct clouds --condition Control

# run synaptic block on a grid of neurons to get the phase boundaries during control
python run_gleak_synblock.py seed1-gleak_synblock-03 --run_seed 1 --struct clouds --condition DAMGO
```

```bash
# generating the burst statistics and count number of tonic, bursting, and quiescent neurons in every network sim
python get_burst_stats.py 1 40
python gleak_count_tbq.py
```

Run the run_synblock_clouds.sh script to account for different experimental conditions under synaptic block. Also use the run_synblock_grids.sh script to simulate neurons across a grid in the gNaP and gLeak parameter space, which we will use to generate phase boundaries later. Then execute run_gleak_mods.sh in order to simulate the gNaP modulation experiment on many different network seeds. Once the .pkl data has been generated, the script will run get_gleak_burst_stats.py and gleak_count_tbq.py to generate burst statistics and count tonic, bursting, and quiescent neurons in each network.