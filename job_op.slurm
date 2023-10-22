#!/bin/bash
#SBATCH --job-name=op_job
#SBATCH --nodes=1
#SBATCH --time=08:00:00
#SBATCH --error=op_job.err
#SBATCH --output=op_job.out
#SBATCH --partition=longrun
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=35G
#SBATCH --gres=gpu:4

srun python3 tests.py