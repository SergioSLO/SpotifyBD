import matplotlib.pyplot as plt

sizes = ['1K', '10K', '100K', '1M']
without_indices = [1.3084, 10.2704, 128.9028, 844.1916]
with_indices = [0.7918, 0.8652, 8.6248, 126.5322]

fig, ax = plt.subplots()

ax.plot(sizes, without_indices, 'o-', color='blue', label='Sin índices')
ax.plot(sizes, with_indices, 'o-', color='red', label='Con índices')

ax.set_xlabel('Tamaño de la consulta')
ax.set_ylabel('Costo promedio (ms)')
ax.set_title('Consulta 1')
ax.legend()

plt.show()


# Consulta
sizes = ['1K', '10K', '100K', '1M']
without_indices = [8.0048,  87.4624, 798.1366, 6813.9342]
with_indices = [3.5242, 23.7642, 342.1132, 2999.2062]

fig, ax = plt.subplots()

ax.plot(sizes, without_indices, 'o-', color='blue', label='Sin índices')
ax.plot(sizes, with_indices, 'o-', color='red', label='Con índices')

ax.set_xlabel('Tamaño de la consulta')
ax.set_ylabel('Costo promedio (ms)')
ax.set_title('Consulta 2')
ax.legend()

plt.show()

# Consulta 3
sizes = ['1K', '10K', '100K', '1M']
without_indices = [8.0048, 54.9636, 325.9338, 9677.4636]
with_indices = [2.6008, 15.829, 93.0748, 236.848]

fig, ax = plt.subplots()

ax.plot(sizes, without_indices, 'o-', color='blue', label='Sin índices')
ax.plot(sizes, with_indices, 'o-', color='red', label='Con índices')

ax.set_xlabel('Tamaño de la consulta')
ax.set_ylabel('Costo promedio (ms)')
ax.set_title('Consulta 3')
ax.legend()

plt.show()
