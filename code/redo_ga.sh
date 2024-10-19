#!/bin/bash

# This script runs the Python script with specified arguments
python run_ga.py --eval-interval 10000 --total-timesteps 100000 --pop-size 25 --num-cores 80 --max-evaluations 250 --exp-name "GA_reproduce" --env-name "Walker-v0"
