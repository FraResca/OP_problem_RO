#!/bin/bash
#SBATCH --job-name=tsili_1_2
#SBATCH --nodes=1
#SBATCH --time=08:00:00
#SBATCH --error=tsili_1_2.err
#SBATCH --output=tsili_1_2.out
#SBATCH --partition=longrun
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=35G
#SBATCH --gres=gpu:4

srun python3 testtsili_1_2.py