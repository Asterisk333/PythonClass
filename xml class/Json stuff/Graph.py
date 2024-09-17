import json
import matplotlib.pyplot as plt


def load_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def extract_data_points(json_data):
    x_data = [item["x"] for item in json_data]
    y_data = [item["y"] for item in json_data]
    return x_data, y_data


def plot_data(x, y):
    plt.plot(x, y, marker='o')
    plt.title("Data Points Graph")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.grid(True)
    plt.show()


def main():
    file_path = "sample_data.json"
    json_data = load_json(file_path)
    x_data, y_data = extract_data_points(json_data)
    plot_data(x_data, y_data)


if __name__ == "__main__":
    main()
