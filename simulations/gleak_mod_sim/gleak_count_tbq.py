import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
# import os
import pickle
sys.path.append('..')
import brian_utils.postproc as bup
# import click

# @click.command()
# @click.argument('target', type = str)
def main():
    #files = glob.glob('targeted_damgo_pkls/{target}_gleak_pkls/*synblock*')
    all_seeds = pd.DataFrame(columns=['# ctrl tonic', '# ctrl bursting', '# ctrl quiescent', 
                                      '# damgo tonic', '# damgo bursting', '# damgo quiescent',
                                      '# damgo + gLeak x 0.9 tonic', '# damgo + gLeak x 0.9 bursting', '# damgo + gLeak x 0.9 quiescent',
                                      '# damgo + gLeak x 0.7 tonic', '# damgo + gLeak x 0.7 bursting', '# damgo + gLeak x 0.7 quiescent',
                                      '# damgo + gLeak x 0.5 tonic', '# damgo + gLeak x 0.5 bursting', '# damgo + gLeak x 0.5 quiescent',], index=np.arange(1,41))
    for i in range(1,41):
        with open(f'../data/gleak_synblock_pkls/clouds_pkls/seed{i}-control_clouds_vars.pkl','rb') as fid1:
            control_data = pickle.load(fid1)
        with open(f'../data/gleak_synblock_pkls/clouds_pkls/seed{i}-damgo_clouds_vars.pkl', 'rb') as fid2:
            damgo_data = pickle.load(fid2)
        with open(f'../data/gleak_synblock_pkls/clouds_pkls/seed{i}-damgo_gleak-01_clouds_vars.pkl', 'rb') as fid3:
            damgo_gLeak01_data = pickle.load(fid3)
        with open(f'../data/gleak_synblock_pkls/clouds_pkls/seed{i}-damgo_gleak-03_clouds_vars.pkl', 'rb') as fid4:
            damgo_gLeak03_data = pickle.load(fid4)
        with open(f'../data/gleak_synblock_pkls/clouds_pkls/seed{i}-damgo_gleak-05_clouds_vars.pkl', 'rb') as fid5:
            damgo_gLeak05_data = pickle.load(fid5)
            
        neurons = control_data['neurongroup']
        ts = control_data['spikemonitor']['t']
        spike_idx = control_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        control_cell_int, control_cell_class = bup.find_bursters_pk_ISI(train,300,)

        neurons = damgo_data['neurongroup']
        ts = damgo_data['spikemonitor']['t']
        spike_idx = damgo_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_cell_int, damgo_cell_class = bup.find_bursters_pk_ISI(train,300,)
        
        neurons = damgo_gLeak01_data['neurongroup']
        ts = damgo_gLeak01_data['spikemonitor']['t']
        spike_idx = damgo_gLeak01_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_gLeak01_cell_int, damgo_gLeak01_cell_class = bup.find_bursters_pk_ISI(train,300,)
        
        neurons = damgo_gLeak03_data['neurongroup']
        ts = damgo_gLeak03_data['spikemonitor']['t']
        spike_idx = damgo_gLeak03_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_gLeak03_cell_int, damgo_gLeak03_cell_class = bup.find_bursters_pk_ISI(train,300,)
        
        neurons = damgo_gLeak05_data['neurongroup']
        ts = damgo_gLeak05_data['spikemonitor']['t']
        spike_idx = damgo_gLeak05_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_gLeak05_cell_int, damgo_gLeak05_cell_class = bup.find_bursters_pk_ISI(train,300,)
            
        ctrl_t = len(np.where(control_cell_int == 1)[0]) 
        ctrl_b = len(np.where(control_cell_int == 0)[0])
        ctrl_q = len(np.where(control_cell_int == 2)[0]) 
        
        damgo_t = len(np.where(damgo_cell_int == 1)[0])
        damgo_b = len(np.where(damgo_cell_int == 0)[0]) 
        damgo_q = len(np.where(damgo_cell_int == 2)[0]) 
        
        damgo_gLeak01_t = len(np.where(damgo_gLeak01_cell_int == 1)[0])
        damgo_gLeak01_b = len(np.where(damgo_gLeak01_cell_int == 0)[0]) 
        damgo_gLeak01_q = len(np.where(damgo_gLeak01_cell_int == 2)[0]) 
        
        damgo_gLeak03_t = len(np.where(damgo_gLeak03_cell_int == 1)[0])
        damgo_gLeak03_b = len(np.where(damgo_gLeak03_cell_int == 0)[0]) 
        damgo_gLeak03_q = len(np.where(damgo_gLeak03_cell_int == 2)[0]) 
        
        damgo_gLeak05_t = len(np.where(damgo_gLeak05_cell_int == 1)[0])
        damgo_gLeak05_b = len(np.where(damgo_gLeak05_cell_int == 0)[0]) 
        damgo_gLeak05_q = len(np.where(damgo_gLeak05_cell_int == 2)[0]) 
        
        
        all_seeds.loc[i] = pd.Series({'# ctrl tonic': ctrl_t, '# ctrl bursting': ctrl_b, '# ctrl quiescent': ctrl_q, 
                                      '# damgo tonic': damgo_t, '# damgo bursting': damgo_b, '# damgo quiescent': damgo_q,
                                      '# damgo + gLeak x 0.9 tonic':damgo_gLeak01_t, '# damgo + gLeak x 0.9 bursting':damgo_gLeak01_b, '# damgo + gLeak x 0.9 quiescent':damgo_gLeak01_q,
                                      '# damgo + gLeak x 0.7 tonic':damgo_gLeak03_t, '# damgo + gLeak x 0.7 bursting':damgo_gLeak03_b, '# damgo + gLeak x 0.7 quiescent':damgo_gLeak03_q,
                                      '# damgo + gLeak x 0.5 tonic':damgo_gLeak05_t, '# damgo + gLeak x 0.5 bursting':damgo_gLeak05_b, '# damgo + gLeak x 0.5 quiescent':damgo_gLeak05_q,})
        
        print(i, all_seeds.loc[i])
    
    all_seeds.to_csv(f'gleak_mod_tbq_counts.csv')
    
if __name__=='__main__':
    main()