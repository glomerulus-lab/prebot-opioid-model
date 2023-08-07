#!/bin/bash

for i in {1..40}
    do  
        python run_gleak_synblock.py seed$i-control_clouds --run_seed $i --condition Control --struct clouds
        python run_gleak_synblock.py seed$i-damgo_clouds --run_seed $i --condition DAMGO --struct clouds
        #python run_gleak_synblock.py seed$i-gleak-01_clouds --run_seed $i --g_leak_str -0.1 --condition G_Leak --struct clouds
        python run_gleak_synblock.py seed$i-damgo_gleak-01_clouds --run_seed $i --g_leak_str -0.1 --condition DAMGO+G_Leak --struct clouds
        #python run_gleak_synblock.py seed$i-gleak-03_clouds --run_seed $i --g_leak_str -0.3 --condition G_Leak --struct clouds
        python run_gleak_synblock.py seed$i-damgo_gleak-03_clouds --run_seed $i --g_leak_str -0.3 --condition DAMGO+G_Leak --struct clouds
        #python run_gleak_synblock.py seed$i-gleak-05_clouds --run_seed $i --g_leak_str -0.5 --condition G_Leak --struct clouds
        python run_gleak_synblock.py seed$i-damgo_gleak-05_clouds --run_seed $i --g_leak_str -0.5 --condition DAMGO+G_Leak --struct clouds
    done

python run_gleak_synblock.py seed$i-control_grid --run_seed $i --struct clouds --hyp_opioid 3 --syn_shut 0.3 --struct grid
python run_gleak_synblock.py seed$i-damgo_grid --run_seed $i --condition DAMGO --hyp_opioid 3 --syn_shut 0.3 --struct grid

#python run_gleak_synblock.py seed$i-gleak_control_clouds --run_seed $i --struct clouds --hyp_opioid 3 --syn_shut 0.3 
#python run_gleak_synblock.py seed$i-gleak_damgo_clouds --run_seed $i --condition DAMGO --hyp_opioid 3 --syn_shut 0.3 --struct clouds
#python run_gleak_synblock.py seed$i-gleak_gnap01_clouds --run_seed $i --g_leak_str 0.1 --hyp_opioid 3 --syn_shut 0.3 --condition G_NaP --struct #clouds
#python run_gleak_synblock.py seed$i-gleak_damgo_gnap01_clouds --run_seed $i --g_leak_str 0.1 --hyp_opioid 3 --syn_shut 0.3 --condition DAMGO+G_NaP -#-struct clouds
#python run_gleak_synblock.py seed$i-gleak_gnap03_clouds --run_seed $i --g_leak_str 0.3 --hyp_opioid 3 --syn_shut 0.3 --condition G_NaP --struct #clouds
#python run_gleak_synblock.py seed$i-gleak_damgo_gnap03_clouds --run_seed $i --g_leak_str 0.3 --hyp_opioid 3 --syn_shut 0.3  --condition DAMGO+G_NaP #--struct clouds
#python run_gleak_synblock.py seed$i-gleak_gnap05_clouds --run_seed $i --g_leak_str 0.5 --hyp_opioid 3 --syn_shut 0.3 --condition G_NaP --struct #clouds
#python run_gleak synblock.py seed$i-gleak_damgo_gnap05_clouds --run_seed $i --g_leak_str 0.5 --hyp_opioid 3 --syn_shut 0.3 --condition DAMGO+G_NaP -#-struct clouds