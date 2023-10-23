import matplotlib.pyplot as plt

def generar_histograma(data, title, xlabel, ylabel):
    plt.hist(data, bins=10, color='blue', edgecolor='black')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def generar_grafico_dispersion(x, y, title, xlabel, ylabel):
    plt.scatter(x, y, color='red', marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
