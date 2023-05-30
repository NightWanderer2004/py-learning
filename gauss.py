import os
import numpy as np
import matplotlib.pyplot as plt

folder_path = "./result"
output_folder = "./result-images"

file_list = os.listdir(folder_path)

for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, 'r') as file:
        values = [float(line.strip()) for line in file.readlines()]

    mu, std = np.mean(values), np.std(values)
    plt.hist(values, bins='auto', density=True)

    x = np.linspace(min(values), max(values), 100)
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / std)**2)
    plt.plot(x, y, 'r-', linewidth=2)

    plt.title(file_name)
    plt.xlabel('u')
    plt.ylabel('n')

    save_path = os.path.join(
        output_folder, os.path.splitext(file_name)[0] + '.png')

    plt.savefig(save_path)
    plt.savefig(save_path)
    plt.clf()

print("Images saved to ./result-images")
