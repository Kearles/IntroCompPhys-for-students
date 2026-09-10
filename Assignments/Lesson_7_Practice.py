
"""import pi


print(pi.__name__)

N = [10**n for n in range(3,7)]

# Get the Leibniz, Sharp and Monte Carlo approximations to pi
π = [(pi.leibniz_pi(cN),pi.Monte_Carlo_pi(cN)) for cN in N]

print(f'{"N":>16}{"Leibniz  π":>16}{"Monte Carlo π":>16}')
for i,cN in enumerate(N):
    print(f'{cN:>16d}{π[i][0]:>16.8f}{π[i][1]:>16.8f}')"""

# asking the user for input
"""N = input("Number of elements: ")
print(N)

# all input is treating like a string
print(type(N))

Ni = int(N)
print(Ni)

Nf = float(N)
print(Nf)

N = float(input("enter a float: "))
print(type(N))


# we can only write strings to files, so we must convert on input and output

for line in lines:
    a = int(line)
    b = a**2
    out_file.write('%d' % b)
out_file.close() """

#There is a file in the data directory called sho_energy.dat.  The line contains column headings with units in kelvin.

#The next set of lines contain quantum Monte Carlo measurements for the kinetic and potential energy of the simple harmonic osscilator at $T = 0.5~\mathrm{K}$ where $\hbar \omega/k_{\mathrm{B}} = 1$.  The exact answer is known to be:
#\begin{equation} E(T) = \frac{\hbar \omega}{2} \coth \frac{\hbar \omega}{2 k_{\mathrm{B}} T}.\end{equation}

#Write a program that loads the file from disk and stores it in a dictionary with labels taken from the column headers.  Compute the average total energy of all lines.


from pathlib import Path

data_file = Path(__file__).resolve().parents[2] / 'data' / 'sho_energy.dat'
with open(data_file, 'r') as in_file:
    lines = [line.split() for line in in_file if line.strip()]

labels = lines[0][1:] if lines[0][0] == '#' else lines[0] 
energy = {label: [] for label in labels}

for values in lines[1:]:
    for label, value in zip(labels, values):
        energy[label].append(float(value))

total_energy = [kinetic + potential
                for kinetic, potential in zip(energy['Kinetic'], energy['Potential'])] 
print(f'Average total energy: {sum(total_energy) / len(total_energy):.6f}') #should show the average of all the numbers in the file

