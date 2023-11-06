#!/bin/bash
#SBATCH --job-name=fe_1
#SBATCH --nodes=1
#SBATCH --time=08:00:00
#SBATCH --error=fe_1.err
#SBATCH --output=fe_1.out
#SBATCH --partition=longrun
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=35G
#SBATCH --gres=gpu:4

srun python3 testfe_1.py