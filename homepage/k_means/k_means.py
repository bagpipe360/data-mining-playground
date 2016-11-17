from matplotlib import style
style.use("ggplot")

from sklearn.cluster import KMeans



def draw_k_means(k, csv):
    graphing_json = {"scatter_plots": {}}
    x_label = csv[0][0]
    y_label = csv[0][1]
    # convert strings to ints in nested lists
    input_data = []
    for i in range(1,len(csv) - 1):
        input_data.append(list(map(float, csv[i])))

    # X = np.array(input_data)
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(input_data)
    labels = kmeans.labels_.tolist()

    graphing_json["centroids"] = kmeans.cluster_centers_.tolist()

    # Loop through k_means labels and assign to separate scatter groups
    for i in range(len(labels)):
        if labels[i] not in graphing_json["scatter_plots"].keys():
            graphing_json["scatter_plots"][labels[i]] = []
        graphing_json["scatter_plots"][labels[i]].append(input_data[i])

    return graphing_json
