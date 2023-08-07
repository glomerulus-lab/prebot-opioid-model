#!/bin/bash


for i in {1..40}
    do
        python run_damgo_ramp.py seed$i-damgo_ramp_pcon_0.01 --run_seed $i --pct_connect 0.02
        rm -r 0000
        python run_damgo_ramp.py seed$i-damgo_ramp_pcon_0.02 --run_seed $i --pct_connect 0.02
        rm -r 0000
        python run_damgo_ramp.py seed$i-damgo_ramp_pcon_0.04 --run_seed $i --pct_connect 0.04
        rm -r 0000
        python run_damgo_ramp.py seed$i-damgo_ramp_pcon_0.08 --run_seed $i --pct_connect 0.08
        rm -r 0000
        python run_damgo_ramp.py seed$i-damgo_ramp_pcon_0.16 --run_seed $i --pct_connect 0.16
        rm -r 0000
    done

for i in 0.01 0.02 0.04 0.08 0.16
    do
        python damgo_ramp_postproc.py 1 40 $i
        
python create_graphs.py 1 40
python tbq_all_networks.py

