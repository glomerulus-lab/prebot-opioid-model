## targeted_damgo_sim/
- ***output_plots/** - contains plots directly outputted from the corresponding simulations
- **compare_sensitivity.ipynb** -compare opioid sensitivity between random, high gLeak, and low gLeak MOR targets. Output sensitivity values into **thresholds.csv**
- **targeted_damgo.py** - code for running the MOR targeting experiment, outputs traces and saves data into .pkl files
- **targeted_damgo_synblock.py** - run the network with specified MOR target and synapses blocked
- **targeted_damgo_ramp.py** - run the network with opioids gradually ramping up from 0 pA to 8 pA onto specified MOR target
- **tbq_all_networks.py** - script for counting tonic, bursting, and quiescent neurons in each network, outputs into **high_gl_ctrl_damgo_tbq_counts.csv** and **low_gl_ctrl_damgo_tbq_counts.csv**
- **run_targeted_damgo.sh** - bash script to simulate many network seeds, both with and without synapses
- **run_targeted_damgo_ramps.sh** - same utility as run_targeted_damgo.sh, but with gradual opioid ramping

### Running the experiment
targeted_damgo.py and targeted_damgo_ramp.py arguments:
- ```prefix```: the name of the run, which is used for data/figure saving purposes. (This is always the first argument)
- ```run_seed```: network seed to be simulated
- ```g_leak_str```: The amount to increase or decrease $g_{Leak}$ by (e.g. pass in 0.3 for a 30% increase, -0.3 for a 30% decrease).
- ```hyp_opioid```: the opioid dosage given when DAMGO is turned on (pA), default value is 4 pA
- ```syn_shut```: the maximum decrease in synaptic strength [0,1] when DAMGO is turned on, default value is 0.5 (meaning that synaptic strength decreases by half)
- ```target```: choose 'high' for MOR on neurons with high $g_{Leak}$ values or 'low' for MOR on neurons with low $g_{Leak}$ values

targeted_damgo_synblock.py arguments are the same as above, but also with:
- ```struct```: choose 'clouds' (which refers to the two-cloud population of the network in gNaP/targeted_damgo space) or 'grid' to generate neurons across a grid of gNaP and gLeak values (for computing phase boundaries)
- ```condition```: choose 'Control', 'DAMGO', 'G_Leak', or 'DAMGO+G_Leak'

<!-- #### Example invocations:
```bash
# increasing G_Leak by 30%
python targeted_damgo_mod.py seed1-targeted_damgo-03 --run_seed 1 --g_leak_str 0.3

# decreasing G_Leak by 30% (note: this effect is clearer when the opioid and synaptic shutdown isn't as strong)
python targeted_damgo_mod.py seed1-targeted_damgo-03 --run_seed 1 --g_leak_str -0.3 --hyp_opioid 3 --syn_shut 0.3

# run synaptic block on network seed 1 when DAMGO and the G_Leak -30% perturbation are both on
python targeted_damgo_synblock.py seed1-targeted_damgo_synblock-03 --run_seed 1 --g_leak_str -0.3 --struct clouds --condition DAMGO+G_Leak

# run synaptic block on a grid of neurons to get the phase boundaries during control
python targeted_damgo_synblock.py seed1-targeted_damgo_synblock-03 --run_seed 1 --struct clouds --condition Control

# run synaptic block on a grid of neurons to get the phase boundaries during control
python targeted_damgo_synblock.py seed1-targeted_damgo_synblock-03 --run_seed 1 --struct clouds --condition DAMGO
``` -->

