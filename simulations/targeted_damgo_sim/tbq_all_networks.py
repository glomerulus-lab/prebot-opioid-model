#!/usr/bin/env python
# coding: utf-8

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
# import os
import pickle
sys.path.append('..')
import brian_utils.postproc as bup
import click

@click.command()
@click.argument('experiment', type = str)
@click.option('target', type = str, default=None)
def main(target):
    #files = glob.glob('targeted_damgo_pkls/{target}_gleak_pkls/*synblock*')
    all_seeds = pd.DataFrame(columns=['ctrl_t_count', 'ctrl_b_count', 'ctrl_q_count', 'damgo_t_count', 'damgo_b_count', 'damgo_q_count'], index=np.arange(1,41))
    for i in range(1,41):
        with open(f'../data/targeted_damgo_pkls/{target}_gleak_pkls/seed{i}-control-{target}_gl_synblock_vars.pkl','rb') as fid1:
            control_data = pickle.load(fid1)
        with open(f'../data/targeted_damgo_pkls/{target}_gleak_pkls/seed{i}-damgo-{target}_gl_synblock_vars.pkl', 'rb') as fid2:
            damgo_data = pickle.load(fid2)
            
        neurons = control_data['neurongroup']
        ts = control_data['spikemonitor']['t']
        spike_idx = control_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        control_cell_int, control_cell_class = bup.find_bursters_pk_ISI(train,300,)

        #state = damgo_data['statemonitor']
        neurons = damgo_data['neurongroup']
        ts = damgo_data['spikemonitor']['t']
        spike_idx = damgo_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_cell_int, damgo_cell_class = bup.find_bursters_pk_ISI(train,300,)
            
        ctrl_t = len(np.where(control_cell_int == 1)[0]) 
        ctrl_b = len(np.where(control_cell_int == 0)[0])
        ctrl_q = len(np.where(control_cell_int == 2)[0]) 
        
        damgo_t = len(np.where(damgo_cell_int == 1)[0])
        damgo_b = len(np.where(damgo_cell_int == 0)[0]) 
        damgo_q = len(np.where(damgo_cell_int == 2)[0]) 
        
        all_seeds.loc[i] = pd.Series({'ctrl_t_count':ctrl_t, 'ctrl_b_count':ctrl_b, 'ctrl_q_count':ctrl_q, 'damgo_t_count':damgo_t, 'damgo_b_count':damgo_b, 'damgo_q_count':damgo_q})
        
        print(i, all_seeds.loc[i])
    
    all_seeds.to_csv(f'{target}_gl_ctrl_damgo_tbq_counts.csv')
    
if __name__=='__main__':
    main()