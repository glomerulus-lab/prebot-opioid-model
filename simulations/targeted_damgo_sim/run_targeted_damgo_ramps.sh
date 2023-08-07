#!/bin/bash

for i in {1..40}
    do
        python targeted_damgo_ramp_synblock.py seed$i-damgo-high_gl_ramp --run_seed $i --target high 
        rm -r 0001
        python targeted_damgo_ramp_synblock.py seed$i-damgo-low_gl_ramp --run_seed $i --target low
        rm -r 0001
    done

