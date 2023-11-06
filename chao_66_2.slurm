#!/bin/bash
#SBATCH --job-name=chao_64_2
#SBATCH --nodes=1
#SBATCH --time=08:00:00
#SBATCH --error=chao_64_2.err
#SBATCH --output=chao_64_2.out
#SBATCH --partition=longrun
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=35G
#SBATCH --gres=gpu:4

srun python3 testchao_66_2.py