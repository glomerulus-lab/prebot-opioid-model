import pandas as pd
import numpy as np
import pickle
import networkx as nx
import brian2
from brian2 import *
sys.path.append('..')
import brian_utils.postproc as bup
import matplotlib
import matplotlib.pyplot as plt
import glob
import re
import io
import os
import sys 


def main(run_seeds):
    f = plt.figure(figsize= (6,5))
    f.tight_layout()
    g = f.add_gridspec(4, 1)
    
    # plot example sims w/ burst detection
    # sim w/ positive g_nap_str
    with open(f'../../prebot_opioid_data/damgo_ramp_pkls/pcon_0.02/seed{run_seeds[0]}-damgo_ramp_pcon_0.02_vars.pkl','rb') as fid1:
        pos_gnap_data = pickle.load(fid1)
    rate1 = pos_gnap_data['ratemonitor']
    
    binsize = 25 * ms 
    smoothed_pop_rate = bup.smooth_saved_rate(rate1, binsize)
    burst_stats = bup.pop_burst_stats(rate1['t'], smoothed_pop_rate, height = 4, prominence = 10)
    
    # mark burst peaks
    ax0 = f.add_subplot(g[0,0])
    plt.plot(rate1['t'], smoothed_pop_rate, 'k', linewidth=1, alpha=0.5)
    #plt.xlabel('Time (s)')
    #plt.ylabel('FR\n(Hz/cell)')
    plt.xticks([])
    plt.xlim(0,600)
    plt.ylim(0,50)
    for thresh in range(10,16):
        plt.axvspan(burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Onset Times'], burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Offset Times'], color='lightsteelblue', alpha=0.3, lw=0)
    plt.plot(burst_stats['Peak Times'], smoothed_pop_rate[burst_stats['Peak Samples']], ".", c='tab:gray')
    
    with open(f'../../prebot_opioid_data/damgo_ramp_pkls/pcon_0.04/seed{run_seeds[1]}-damgo_ramp_pcon_0.04_vars.pkl','rb') as fid1:
        pos_gnap_data = pickle.load(fid1)
    rate1 = pos_gnap_data['ratemonitor']
    
    binsize = 25 * ms
    smoothed_pop_rate = bup.smooth_saved_rate(rate1, binsize)
    burst_stats = bup.pop_burst_stats(rate1['t'], smoothed_pop_rate, height = 4, prominence = 10)
    
#     for thresh in range(10,16):
#         plt.plot(burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Peaks'], smoothed_pop_rate[burst_stats['Peak Samples']], color = 'g', '.')
    
    # mark burst peaks
    ax1 = f.add_subplot(g[1,0], sharex=ax0)
    plt.plot(rate1['t'], smoothed_pop_rate, 'k', linewidth=1, alpha=0.5)
    #plt.xlabel('Time (s)')
    #plt.ylabel('FR\n(Hz/cell)')
    plt.xlim(0,600)
    plt.xticks([])
    plt.ylim(0,50)
    for thresh in range(10,16):
        plt.axvspan(burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Onset Times'], burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Offset Times'], color='lightsteelblue', alpha=0.3, lw=0)
    plt.plot(burst_stats['Peak Times'], smoothed_pop_rate[burst_stats['Peak Samples']], ".", c='tab:gray')
    
    with open(f'../../prebot_opioid_data/damgo_ramp_pkls/pcon_0.08/seed{run_seeds[2]}-damgo_ramp_pcon_0.08_vars.pkl','rb') as fid1:
        pos_gnap_data = pickle.load(fid1)
    rate1 = pos_gnap_data['ratemonitor']
    
    binsize = 25 * ms
    smoothed_pop_rate = bup.smooth_saved_rate(rate1, binsize)
    burst_stats = bup.pop_burst_stats(rate1['t'], smoothed_pop_rate, height = 4, prominence = 10)
    
#     for thresh in range(10,16):
#         plt.plot(burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Peaks'], smoothed_pop_rate[burst_stats['Peak Samples']], color = 'm', '.')
    
    # mark burst peaks
    ax2 = f.add_subplot(g[2,0], sharex=ax0)
    plt.plot(rate1['t'], smoothed_pop_rate, 'k', linewidth=1, alpha=0.5)
    #plt.xlabel('Time (s)')
    #plt.ylabel('FR\n(Hz/cell)')
    plt.xlim(0,600)
    plt.xticks([])
    plt.ylim(0,50)
    for thresh in range(10,16):
        plt.axvspan(burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Onset Times'], burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Offset Times'], color='lightsteelblue', alpha=0.3, lw=0)
    plt.plot(burst_stats['Peak Times'], smoothed_pop_rate[burst_stats['Peak Samples']], ".", c='tab:gray')
    
    with open(f'../../prebot_opioid_data/damgo_ramp_pkls/pcon_0.16/seed{run_seeds[3]}-damgo_ramp_pcon_0.16_vars.pkl','rb') as fid1:
        pos_gnap_data = pickle.load(fid1)
    rate1 = pos_gnap_data['ratemonitor']
    
    binsize = 25 * ms
    smoothed_pop_rate = bup.smooth_saved_rate(rate1, binsize)
    burst_stats = bup.pop_burst_stats(rate1['t'], smoothed_pop_rate, height = 4, prominence = 10)
    
#     for thresh in range(10,16):
#         plt.plot(burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Peaks'], smoothed_pop_rate[burst_stats['Peak Samples']], color = 'gold', '.')
    
    # mark burst peaks
    ax3 = f.add_subplot(g[3,0], sharex=ax0)
    plt.plot(rate1['t'], smoothed_pop_rate, 'k', linewidth=1, alpha=0.5)
    plt.xlabel('Time (10 minutes)')
    #plt.ylabel('FR\n(Hz/cell)')
    plt.xlim(0,600)
    plt.xticks([])
    plt.ylim(0,50)
    for thresh in range(10,16):
        plt.axvspan(burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Onset Times'], burst_stats[burst_stats['Peaks'] >= thresh].iloc[-1]['Offset Times'], color='lightsteelblue', alpha=0.3, lw=0)
    plt.plot(burst_stats['Peak Times'], smoothed_pop_rate[burst_stats['Peak Samples']], ".", c='tab:gray')
    #f.supylabel('FR\n(Hz/cell)')

    plt.savefig(f'fig3_traces.png', dpi=300)
    
if __name__ == "__main__":
    main([2,2,2,1])