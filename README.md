# VoxSurf - DEI Hackathon: https://deihackathon2025.com/

Surf the web with Voice and AI Agentic powered accessibility.

## Code Base
- Frontend code on root level
- Backend folder has desktop application source code

## Development Guide
Below are instructions for development purposes.

### Local Set Up
conda create --name voxsurf-package python=3.9.7
conda activate voxsurf-package
conda install -c conda-forge poetry
poetry install
poetry shell
sudo python backend/src/main.py

### Installing packages
poetry install <package name>

## Packing application
cd backend
poetry shell
pyinstaller --clean --windowed src/main.py

### Demo
https://youtu.be/fF8kPXiXp9Y

