#!/bin/bash
#SBATCH --job-name=tsili_2_1
#SBATCH --nodes=1
#SBATCH --time=08:00:00
#SBATCH --error=tsili_2_1.err
#SBATCH --output=tsili_2_1.out
#SBATCH --partition=longrun
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=35G
#SBATCH --gres=gpu:4

srun python3 testtsili_2_1.py