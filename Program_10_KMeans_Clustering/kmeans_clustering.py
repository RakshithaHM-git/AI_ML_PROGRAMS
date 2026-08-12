import numpy as np

print("Name: Rakshitha H M")
print("USN: 24BECS139")
print()


def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))


class KMeans:

    def __init__(self, k=2, max_iters=100):
        self.k = k
        self.max_iters = max_iters

    def fit(self, X):

        # Pick random initial centroids
        idx = np.random.choice(X.shape[0], self.k, replace=False)
        self.centroids = X[idx]

        for _ in range(self.max_iters):

            # Assign clusters
            self.labels = np.array([
                np.argmin([euclidean_distance(x, c) for c in self.centroids])
                for x in X
            ])

            # Recompute centroids
            new_centroids = np.array([
                X[self.labels == i].mean(axis=0)
                if len(X[self.labels == i]) > 0
                else self.centroids[i]
                for i in range(self.k)
            ])

            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids

        return self.labels


def silhouette_score_simple(X, labels):

    # Simple Silhouette Score
    scores = []

    for i, x in enumerate(X):
        cluster_index = labels[i]

        same_cluster = X[labels == cluster_index]
        other_cluster = X[labels != cluster_index]

        if len(same_cluster) > 1:
            a = np.mean([
                euclidean_distance(x, point)
                for point in same_cluster
                if not np.array_equal(x, point)
            ])
        else:
            a = 0

        if len(other_cluster) > 0:
            b = np.min([
                np.mean([
                    euclidean_distance(x, point)
                    for point in X[labels == c]
                ])
                for c in set(labels)
                if c != cluster_index
            ])
        else:
            b = 0

        if max(a, b) == 0:
            scores.append(0)
        else:
            scores.append((b - a) / max(a, b))

    return np.mean(scores)


# Example Usage
if __name__ == "__main__":

    X = np.array([
        [1, 2],
        [1, 4],
        [1, 0],
        [10, 2],
        [10, 4],
        [10, 0]
    ])

    print("Dataset:")
    print(X)

    km = KMeans(k=2)
    labels = km.fit(X)

    score = silhouette_score_simple(X, labels)

    print("\nAssigned Labels:")
    print(labels)

    print("\nCluster Centroids:")
    print(km.centroids)

    print("\nCalculated Silhouette Validation Score:")
    print(score)