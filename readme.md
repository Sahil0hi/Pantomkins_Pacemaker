# QRS Pacemaker Simulation

This project implements a comprehensive simulation of a **VVIR Pacemaker** integrated with a real-time **Pan-Tompkins QRS detection algorithm**. It allows for the simulation of cardiac sensing, pacing logic, and rate modulation, accompanied by a rich visualization dashboard.

##  Project Overview

The system is designed to simulate a closed-loop biomedical device:
1.  **Sensing**: It processes raw ECG signals to detect R-peaks (heartbeats) using a C-optimized implementation of the Pan-Tompkins algorithm.
2.  **Logic**: It implements standard pacemaker timing cycles (NBG Code: **VVIR**):
    *   **V**entricle Paced
    *   **V**entricle Sensed
    *   **I**nhibited Response (resets timer on natural beat)
    *   **R**ate Modulation (adjusts pacing rate based on simulated activity)
3.  **Visualization**: A real-time dashboard plots the ECG trace, pacemaker status (Sensing vs. Pacing), and instantaneous heart rate, synchronized with a video animation of a beating heart.

##  Key Features

*   **High-Performance QRS Detection**: Uses a compiled C shared library (`libpantompkins.so`) for efficient real-time signal processing (Bandpass filter, derivative, squaring, moving window integration).
*   **Pacemaker Modes**: 
    *   Supports single-chamber pacing logic.
    *   includes **Rate Modulation** to adapt heart rate to simulated physical activity.
*   **Interactive Visualization**:
    *   Real-time scrolling ECG plot.
    *   Visual markers for Paced beats vs. Natural beats.
    *   Live BPM tracking vs. Target Rate.
    *   Synchronized heart video playback.
*   **Simulation Support**: Can run simulations against synthetic data or standard MIT-BIH arrhythmia database records.

##  Project Structure

*   **`SILPackemaker/`**: Contains the core Python implementation of the pacemaker.
    *   `Pacemaker.py`: Main device class handling the step-by-step simulation.
    *   `PacingLogic.py`: Implements the timing counters and trigger logic.
    *   `RateModulator.py`: Handles adaptive rate calculations based on sensor inputs.
*   **`Qrs_detect/`**: C-based Digital Signal Processing module.
    *   `panTompkins.c`: Core detection algorithm.
    *   `r_peak.py`: Python wrapper for the compiled C library.
*   **`heart_video_final.py`**: The primary demo script that runs the visualization.
*   **`simulate.py`**: Script to run simulations on MIT-BIH database files.
*   **`Assests/`**: Contains media assets for visualization (e.g., `heart2.mp4`).

##  Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd QRSPacemaker
    ```

2.  **Install Dependencies**:
    The project relies on standard scientific Python libraries.
    ```bash
    pip install -r requirements.txt
    ```
    *Key requirements: `numpy`, `matplotlib`, `opencv-python`, `wfdb`, `imageio`.*

3.  **Build C Extension (If needed)**:
    The project includes a precompiled `libpantompkins.so`. If you are on a different architecture (e.g., macOS vs Linux) and encounter errors, you may need to recompile the C code:
    ```bash
    cd Qrs_detect
    gcc -shared -o libpantompkins.so -fPIC panTompkins.c
    ```

##  Usage

### 1. Run the Heart Visualization Demo
This is the main showcase of the project, displaying the ECG and Pacemaker status in real-time.
```bash
python heart_video_final.py
```

### 2. Run Simulation on MIT-BIH Data
To test the pacemaker logic against real-world arrhythmia data:
```bash
python simulate.py
```
*(Note: Requires internet access to download MIT-BIH records via `wfdb`)*

##  References

*   **Pan-Tompkins Algorithm**: Pan, J., & Tompkins, W. J. (1985). "A real-time QRS detection algorithm." *IEEE Transactions on Biomedical Engineering*, 32(10), 230–236.
*   **Base Implementation**: [PanTompkinsQRS by rafaelmmoreira](https://github.com/rafaelmmoreira/PanTompkinsQRS)
