import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Function to read the input text file and parse the data
def read_input_file(file_path):
    forces = []
    accs = []
    millis = []
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if len(line) == 3:
                forces.append(float(line[0]))
                accs.append(-1*float(line[1]))
                millis.append(int(line[2]))
    
    return forces, accs, millis

# Read input file
forces, accs, millis = read_input_file('Trial1_Slow')
print('Forces:', len(forces))
print('Acceleration:', len(accs))
print('Time:', len(millis))

# normalize time w.r.t initial time
# Convert milliseconds to seconds for integration
millis = millis - np.ones(len(millis)) * millis[0]
time_sec = np.array(millis) / 1000
print('Time [s]:', len(time_sec))

accel_bar = [0, accs[0]*(time_sec[1] - time_sec[0])]
for i in range(2, len(time_sec)):
    accel_bar.append(accel_bar[i-1] + accs[i-1] * (time_sec[i] - time_sec[i-1]))

# Integrate acceleration to get velocity (assuming initial velocity is 0)
velocity = [0]
for i in range(1, len(accel_bar)):
    velocity.append(accel_bar[i]+.5*accs[i]*(time_sec[i]-time_sec[i-1]))

# Create dataframe for velocity
velocity_data = pd.DataFrame({'Velocity [m/s]': velocity, 'Time [s]': time_sec})

# Plot velocity vs time
plt.figure(figsize=(10, 6))
plt.plot(velocity_data['Time [s]'], velocity_data['Velocity [m/s]'], marker='o', linestyle='-')
plt.title('Velocity vs Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)
plt.savefig('velocity_vs_time_plot.png')
plt.show()

##################################################

# Create pandas DataFrame
# df = pd.DataFrame([forces,accs,millis], columns=["Force [lbs]", "Acc W/ G [m/s^2]", "Millis [ms]"])

# # Plot 1: Force in pounds vs time in ms
# plt.figure(figsize=(8, 6))
# plt.plot(df["Millis [ms]"], df["Force [lbs]"], marker='o', linestyle='-')
# plt.title("Force vs Time")
# plt.xlabel("Time (ms)")
# plt.ylabel("Force (lbs)")
# plt.grid(True)
# plt.savefig("force_vs_time.png")
# plt.show()

# # Plot 2: Acceleration w/ G vs time in ms
# plt.figure(figsize=(8, 6))
# plt.plot(df["Millis [ms]"], df["Acc W/ G [m/s^2]"], marker='o', linestyle='-')
# plt.title("Acceleration w/ G vs Time")
# plt.xlabel("Time (ms)")
# plt.ylabel("Acceleration w/ G (m/s^2)")
# plt.grid(True)
# plt.savefig("acceleration_vs_time.png")
# plt.show()

# # Save data to CSV
# df.to_csv("output.csv", index=False)

# Save velocity data to CSV
velocity_data.to_csv('velocity_output.csv', index=False)
