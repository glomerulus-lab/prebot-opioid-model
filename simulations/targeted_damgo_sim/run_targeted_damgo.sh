#!/bin/bash

for i in {1..40}
    do
        python targeted_damgo.py seed$i-damgo-high_gl --run_seed $i --target high --synblock 1
        rm -r 0000
        python targeted_damgo.py seed$i-damgo-low_gl --run_seed $i --target low --synblock 1
        rm -r 0000
        python targeted_damgo.py seed$i-control-high_gl_synblock --run_seed $i --target high --synblock 0 --condition control
        rm -r 0000
        python targeted_damgo.py seed$i-control-low_gl_synblock --run_seed $i --target low --synblock 0 --condition control
        rm -r 0000
        python targeted_damgo.py seed$i-damgo-high_gl_synblock --run_seed $i --target high --synblock 0 --condition DAMGO
        rm -r 0000
        python targeted_damgo.py seed$i-damgo-low_gl_synblock --run_seed $i --target low --synblock 0 --condition DAMGO
        rm -r 0000
    done
