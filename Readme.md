# Quantum Symphony 🎶✨  
A combined **Quantum Art + Quantum Music** generator powered by **Qiskit**, **NumPy**, **Matplotlib**, and **Pygame**.

This project contains two integrated components:

1. **Quantum Radiance** – Generates abstract radiant art using quantum randomness.  
2. **Quantum Aurora** – Produces a melodic quantum-generated tune using Pygame sound synthesis.

This README explains **installation**, **requirements**, **setup**, and **execution steps** for both modules.

---

## 📌 Features

### 🎨 Quantum Radiance (Art Generator)
- Uses Qiskit’s quantum simulator to create randomness.
- Generates a glowing radial-gradient background.
- Adds quantum-dependent particle bursts.
- Saves output as `quantum_radiance_art.png`.

### 🎵 Quantum Aurora (Music Generator)
- Generates melodies using quantum-generated bitstrings.
- Converts bitstring randomness into musical notes.
- Produces harmonic tones using custom sine-wave synthesis.

---

## 🛠️ Requirements

### Install Python  
Python **3.8 – 3.12** is recommended.

Check version:  
```
python --version
```

---

## 📦 Install Dependencies

Run the following command inside your project folder:

```
pip install qiskit qiskit-aer pygame numpy matplotlib
```

If pip is slow on Windows, try:

```
python -m pip install --upgrade pip
```

---

## ▶️ How to Run the Program

The uploaded file is named **Quantum_symphony.py** and contains both modules.

### **1. Run Quantum Radiance (Art Generator)**

```
python Quantum_symphony.py
```

It will:
- Simulate quantum randomness  
- Generate a radiant abstract art  
- Save image as `quantum_radiance_art.png`

You will see a plot window and the saved file in your directory.

---

### **2. Run Quantum Aurora (Music Generator)**

When the script reaches the music section:
- Pygame will initialize  
- A melodic quantum tune will start playing  
- Notes are printed in the console  

Make sure:
- Your speakers are ON  
- Pygame is allowed audio permissions  

---

## 📁 Output Files

| Component | Output |
|----------|--------|
| Quantum Radiance | `quantum_radiance_art.png` |
| Quantum Aurora | Live audio playback + printed notes |

---

## 🧩 File Structure
```
Quantum_symphony.py
README.md   ← (this file)
```

---

## ⚠️ Common Issues

### **Pygame audio error**
Install stable version:
```
pip install pygame==2.1.3
```

### **Qiskit Aer import error**
```
pip install qiskit-aer
```

---

## 🙌 Credits
Created using:
- **Qiskit**
- **NumPy**
- **Matplotlib**
- **Pygame**

Quantum + Art + Music = ⚛️🎨🎶  
Enjoy the quantum symphony!
