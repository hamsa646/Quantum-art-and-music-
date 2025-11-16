#  Quantum Radiance: Abstract Energy Art Generator
# Inspired by quantum measurement randomness and radiant color fields

from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
import matplotlib.pyplot as plt
import numpy as np
import random

# --- Quantum Setup ---
qc = QuantumCircuit(5, 5)
qc.h(range(5))        # Create superposition (randomness)
qc.measure(range(5), range(5))

# --- Quantum Simulation ---
sim = Aer.get_backend('qasm_simulator')
tqc = transpile(qc, sim)
job = sim.run(tqc, shots=256)
result = job.result()
counts = result.get_counts()

# --- Canvas Setup ---
plt.figure(figsize=(10, 12))
plt.axis('off')
plt.title("Quantum Radiance ", fontsize=26, fontweight='bold', color='white')
plt.style.use('dark_background')

# --- Create radiant gradient background ---
size = 1000
x = np.linspace(-1, 1, size)
y = np.linspace(-1.5, 1.5, size)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# Create a radial gradient in warm tones
R_channel = np.exp(-R*2) + 0.3*np.sin(3*R)
G_channel = np.exp(-R*3)
B_channel = np.exp(-R*1.5) + 0.2*np.sin(2*R)
background = np.dstack((R_channel, G_channel*0.4, B_channel*0.8))
plt.imshow(background, extent=[0,1,0,1], origin='lower', alpha=1)

# --- Quantum bursts ---
for state, freq in counts.items():
    # Convert bitstring into position and size
    x_pos = random.random()
    y_pos = random.random()
    size = freq * random.uniform(20, 250)
    color = (
        random.uniform(0.8, 1.0),       # warm reddish tone
        random.uniform(0.3, 0.6),       # touch of gold
        random.uniform(0.0, 0.4)        # deep purple shade
    )
    plt.scatter(x_pos, y_pos, s=size, color=color, alpha=random.uniform(0.4, 0.9))

# --- Add glowing particles for depth ---
for _ in range(60):
    plt.scatter(random.random(), random.random(),
                s=random.uniform(100, 900),
                color=(random.uniform(0.8, 1.0), random.uniform(0.4, 0.6), random.uniform(0.2, 0.5)),
                alpha=random.uniform(0.1, 0.3))

# --- Save and show ---
plt.savefig("quantum_radiance_art.png", dpi=300, bbox_inches='tight')
plt.show()

#  Quantum Aurora – A Melodic Quantum Tune using pygame

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np
import pygame
import time
import random

#  Initialize mixer
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

#  Define base note frequencies (C major scale)
notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

#  Quantum randomness seed
qc = QuantumCircuit(5)
qc.h(range(5))
qc.measure_all()

sim = AerSimulator()
compiled = transpile(qc, sim)
result = sim.run(compiled, shots=64).result()
counts = result.get_counts()

#  Generate melody sequence from bitstrings
sequence = []
for bitstring in counts.keys():
    idx = int(bitstring, 2) % len(notes)
    note = list(notes.keys())[idx]
    sequence.append(note)

#  Define a simple chord progression (C → G → Am → F)
progression = [
    ["C", "E", "G"],
    ["G", "B", "D"],
    ["A", "C", "E"],
    ["F", "A", "C"]
]

#  Function to play a tone with soft harmonics
def play_tone(frequency, duration=0.35, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)

    # smooth harmonic blend
    tone = (
        np.sin(frequency * t * 2 * np.pi)
        + 0.4 * np.sin(2 * frequency * t * 2 * np.pi)
        + 0.2 * np.sin(3 * frequency * t * 2 * np.pi)
    )
    tone *= volume
    sound = np.array([tone, tone]).T
    sound = (sound * 32767).astype(np.int16)
    sound = np.ascontiguousarray(sound)
    pygame.sndarray.make_sound(sound).play()
    time.sleep(duration)

#  Play the full tune
print(" Playing Quantum Aurora... Relax and listen \n")

for note in sequence[:16]:
    # Print instantly
    print(note, end=" ", flush=True)  

    chord = random.choice(progression)
    root_freq = notes[note]
    play_tone(root_freq, duration=0.3)

    # Play chord softly behind melody
    for harmony in chord:
        freq = notes[harmony] * random.choice([0.5, 1, 2])
        play_tone(freq, duration=0.15, volume=0.3)

    time.sleep(random.choice([0.05, 0.1, 0.15]))

print("\n Quantum Aurora complete!")
