#!/bin/bash

for i in {9..9}
    do
        python run_gleak_mod.py seed$i-gleak-05 --run_seed $i --g_leak_str -0.5 
        python run_gleak_mod.py seed$i-gleak-03 --run_seed $i --g_leak_str -0.3 
        python run_gleak_mod.py seed$i-gleak-01 --run_seed $i --g_leak_str -0.1 
        python run_gleak_mod.py seed$i-gleak05 --run_seed $i --g_leak_str 0.5 --hyp_opioid 3 --syn_shut 0.3
        python run_gleak_mod.py seed$i-gleak03 --run_seed $i --g_leak_str 0.3 --hyp_opioid 3 --syn_shut 0.3
        python run_gleak_mod.py seed$i-gleak01 --run_seed $i --g_leak_str 0.1 --hyp_opioid 3 --syn_shut 0.3
    done
