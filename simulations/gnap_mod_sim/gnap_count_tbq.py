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
                                      '# damgo + gNaP x 1.1 tonic', '# damgo + gNaP x 1.1 bursting', '# damgo + gNaP x 1.1 quiescent',
                                      '# damgo + gNaP x 1.3 tonic', '# damgo + gNaP x 1.3 bursting', '# damgo + gNaP x 1.3 quiescent',
                                      '# damgo + gNaP x 1.5 tonic', '# damgo + gNaP x 1.5 bursting', '# damgo + gNaP x 1.5 quiescent',], index=np.arange(1,41))
    for i in range(1,41):
        with open(f'../data/gnap_synblock_pkls/clouds_pkls/seed{i}-control_clouds_vars.pkl','rb') as fid1:
            control_data = pickle.load(fid1)
        with open(f'../data/gnap_synblock_pkls/clouds_pkls/seed{i}-damgo_clouds_vars.pkl', 'rb') as fid2:
            damgo_data = pickle.load(fid2)
        with open(f'../data/gnap_synblock_pkls/clouds_pkls/seed{i}-damgo_gnap01_clouds_vars.pkl', 'rb') as fid3:
            damgo_gnap01_data = pickle.load(fid3)
        with open(f'../data/gnap_synblock_pkls/clouds_pkls/seed{i}-damgo_gnap03_clouds_vars.pkl', 'rb') as fid4:
            damgo_gnap03_data = pickle.load(fid4)
        with open(f'../data/gnap_synblock_pkls/clouds_pkls/seed{i}-damgo_gnap05_clouds_vars.pkl', 'rb') as fid5:
            damgo_gnap05_data = pickle.load(fid5)
            
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
        
        neurons = damgo_gnap01_data['neurongroup']
        ts = damgo_gnap01_data['spikemonitor']['t']
        spike_idx = damgo_gnap01_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_gnap01_cell_int, damgo_gnap01_cell_class = bup.find_bursters_pk_ISI(train,300,)
        
        neurons = damgo_gnap03_data['neurongroup']
        ts = damgo_gnap03_data['spikemonitor']['t']
        spike_idx = damgo_gnap03_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_gnap03_cell_int, damgo_gnap03_cell_class = bup.find_bursters_pk_ISI(train,300,)
        
        neurons = damgo_gnap05_data['neurongroup']
        ts = damgo_gnap05_data['spikemonitor']['t']
        spike_idx = damgo_gnap05_data['spikemonitor']['i']
        train = bup.create_train(ts,spike_idx)
        damgo_gnap05_cell_int, damgo_gnap05_cell_class = bup.find_bursters_pk_ISI(train,300,)
            
        ctrl_t = len(np.where(control_cell_int == 1)[0]) 
        ctrl_b = len(np.where(control_cell_int == 0)[0])
        ctrl_q = len(np.where(control_cell_int == 2)[0]) 
        
        damgo_t = len(np.where(damgo_cell_int == 1)[0])
        damgo_b = len(np.where(damgo_cell_int == 0)[0]) 
        damgo_q = len(np.where(damgo_cell_int == 2)[0]) 
        
        damgo_gnap01_t = len(np.where(damgo_gnap01_cell_int == 1)[0])
        damgo_gnap01_b = len(np.where(damgo_gnap01_cell_int == 0)[0]) 
        damgo_gnap01_q = len(np.where(damgo_gnap01_cell_int == 2)[0]) 
        
        damgo_gnap03_t = len(np.where(damgo_gnap03_cell_int == 1)[0])
        damgo_gnap03_b = len(np.where(damgo_gnap03_cell_int == 0)[0]) 
        damgo_gnap03_q = len(np.where(damgo_gnap03_cell_int == 2)[0]) 
        
        damgo_gnap05_t = len(np.where(damgo_gnap05_cell_int == 1)[0])
        damgo_gnap05_b = len(np.where(damgo_gnap05_cell_int == 0)[0]) 
        damgo_gnap05_q = len(np.where(damgo_gnap05_cell_int == 2)[0]) 
        
        
        all_seeds.loc[i] = pd.Series({'# ctrl tonic': ctrl_t, '# ctrl bursting': ctrl_b, '# ctrl quiescent': ctrl_q, 
                                      '# damgo tonic': damgo_t, '# damgo bursting': damgo_b, '# damgo quiescent': damgo_q,
                                      '# damgo + gNaP x 1.1 tonic':damgo_gnap01_t, '# damgo + gNaP x 1.1 bursting':damgo_gnap01_b, '# damgo + gNaP x 1.1 quiescent':damgo_gnap01_q,
                                      '# damgo + gNaP x 1.3 tonic':damgo_gnap03_t, '# damgo + gNaP x 1.3 bursting':damgo_gnap03_b, '# damgo + gNaP x 1.3 quiescent':damgo_gnap03_q,
                                      '# damgo + gNaP x 1.5 tonic':damgo_gnap05_t, '# damgo + gNaP x 1.5 bursting':damgo_gnap05_b, '# damgo + gNaP x 1.5 quiescent':damgo_gnap05_q,})
        
        print(i, all_seeds.loc[i])
    
    all_seeds.to_csv(f'gnap_mod_tbq_counts.csv')
    
if __name__=='__main__':
    main()