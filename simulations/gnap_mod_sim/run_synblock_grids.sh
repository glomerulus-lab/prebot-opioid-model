#!/bin/bash

python run_gnap_synblock.py control_grid --run_seed 1 --condition Control --struct grid
python run_gnap_synblock.py damgo_grid --run_seed 1 --condition DAMGO --struct grid


