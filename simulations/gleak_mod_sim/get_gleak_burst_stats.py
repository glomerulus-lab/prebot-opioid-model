# Use this script to generate and concatenate burst statistics for your runs 

import os
import seaborn as sns
import scipy.io.matlab as sio
import click
import glob
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pltp
sys.path.append('..')
from brian2 import *
import brian_utils.postproc as bup
import brian_utils.viz as bviz
import pandas as pd
import pickle
import scipy.signal
        
# Adding the phase of the experiment to the burst statistics
def add_conditions(df):
    # Perturbation times
    condition_times = [0,30,60,70,100,110,140,150,180,190,220,240] # for longer runs

    # 0-30 s, other 10 s gaps: Transient
    # 30-60 s: Control 
    # 70-100 s: DAMGO
    # 110-140 s: Wash
    # 150-180 s: G_Leak
    # 190-220 s: DAMGO + G_Leak
    # 220-224 s: synaptic block
    condition_labels = ['Transient', 'Control', 'Transient','DAMGO','Transient','Wash','Transient',
                        r'$G_{Leak}$', 'Transient', r'DAMGO + $G_{Leak}$', 'Block',]

    burst_conditions = []

    for ii in range(len(condition_times)-1):
      t0 = condition_times[ii]
      tf = condition_times[ii+1]
      condition = condition_labels[ii]

      for burst_time in df['Onset Times']:
          if burst_time < tf and burst_time > t0:
              burst_condition = condition
              burst_conditions.append(burst_condition)

    df['Condition'] = burst_conditions

# Concatenating together the data from each run (varying by G_Leak strength) for one particular network seed
def one_network_df(run_seed, exp_type):
    # change filepath and/or naming accordingly (this can be a common cause of bugs)
    files = glob.glob(f'{exp_type}_pkls/seed{run_seed}-gleak*.pkl')
    
    gleak_neg05 = 'gleak-05'
    gleak_neg04 = 'gleak-04'
    gleak_neg03 = 'gleak-03'
    gleak_neg02 = 'gleak-02'
    gleak_neg01 = 'gleak-01'
    gleak_01 = 'gleak01'
    gleak_02 = 'gleak02'
    gleak_03 = 'gleak03'
    gleak_04 = 'gleak04'
    gleak_05 = 'gleak05'

    dfs = []
    print(f'Processing network seed {run_seed}...')
    for file in files:
        with open(file,'rb') as fid:
            data = pickle.load(fid)
            
        rate = data['ratemonitor']
        binsize = 50 * ms
        smoothed_pop_rate = bup.smooth_saved_rate(rate, binsize)
        df = bup.pop_burst_stats(rate['t'], smoothed_pop_rate, height = 4, prominence = 10)
        
        df['filename'] = os.path.basename(file)
        add_conditions(df)    
        
        df['run_seed'] = run_seed
 
        if gleak_neg05 in df.at[0, 'filename']:
            df[r'$G_{Leak}$ str'] = -0.5

        if gleak_neg03 in df.at[0, 'filename']:
            df[r'$G_{Leak}$ str'] = -0.3

        if gleak_neg01 in df.at[0, 'filename']:
            df[r'$G_{Leak}$ str'] = -0.1

        if gleak_01 in df.at[0, 'filename']:
            df[r'$G_{Leak}$ str'] = 0.1

        if gleak_03 in df.at[0, 'filename']:
            df[r'$G_{Leak}$ str'] = 0.3

        if gleak_05 in df.at[0, 'filename']:
            df[r'$G_{Leak}$ str'] = 0.5

        dfs.append(df)

    network_df = pd.concat(dfs, ignore_index = True)
    network_df.head()
    return network_df

# concatenating all the data together and 
def concat_networks(seed_list, exp_type):
    dfs = []
    for i in range(len(seed_list)):
        network_df = one_network_df(seed_list[i], exp_type)
        dfs.append(network_df)
        
    df = pd.concat(dfs, ignore_index = True)
    df.reset_index()
    df.to_csv(f'seed{seed_list[0]}to{seed_list[len(seed_list)-1]}_{exp_type}_burst_stats.csv')
    
@click.command()
@click.argument('first_seed', type = int)
@click.argument('last_seed', type = int)
@click.option('--exp_type', type = str, default = 'gleak_mod') # gleak_mod, high_con, damgo_to_low_gleak, damgo_to_high_gleak
def main(first_seed,last_seed, exp_type):    
    concat_networks(list(range(first_seed, last_seed+1)), exp_type)
    
if __name__=='__main__':
    main()
    
# need seed26-gleak03, seed29-gleak05, seed39-gleak01, seed8 all but gleak-05, seed9 all