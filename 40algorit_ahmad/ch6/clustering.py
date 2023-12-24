'''
K-Means Clustering in python.
Author: Nat Hawkins
Date (YYYY-MM-DD): 2023-12-23
'''

# Imports ----------------------------------------------------------------------
from distances import euclideanDistance, cosineDistance, manhattanDistance
from typing import Iterable
import random
import matplotlib.pyplot as plt

# Functions --------------------------------------------------------------------
class KMeans:
    """
    KMeans clustering implemented in python.
    """
    def __init__(self, k, 
                 max_iter = 1000,
                 distance = euclideanDistance):
        '''
        Initialize KMeans algorithm.
        
        Parameters
        ----------
        - k (int): Number of centroids.
        - max_iter (int): Maximum number of iterations to perform. Default 1000.
        - distance (method): Function to use for calculating distance. Default euclideanDistance().
        '''
        self.k = k
        self.max_iter = max_iter
        self.distance = distance
        self.precision = 5
        self.data = None

    def _stable(self, new_centroids, threshold = 1e-10):
        '''
        Determines the stability of centroids by comparing the maximum difference 
        between the old and new centroids against a given threshold.

        Parameters
        ----------
        - self: The instance object.
        - new_centroids (Iterable): New centroids to be compared.
        - threshold (float, optional): The threshold value for stability comparison. Default 1e-10.

        Returns:
        - bool: True if the maximum difference between corresponding elements 
                of old and new centroids is less than the threshold, 
                indicating stability. False otherwise.
        '''
        return max(max(abs(x_i - y_i) for x_i, y_i in zip(old_centroid, new_centroid)) for old_centroid, new_centroid in zip(self.centroids, new_centroids)) < threshold

    def fit(self, X, store = True, random_state = 8675309):
        '''
        Compute cluster centroids and assign samples to clusters.

        Parameters
        ----------
        - X (Iterable): Iterable of shape (number of samples, number of features per sample)
        - store (bool): Store input data X for visualization. Default True.
        - random_state (int): Integer random seed to set for reproducibility. Default 8675309.
        '''
        # Check to see if training data should be stored
        if store:
            self.data = X

        # Set seed
        random.seed(random_state)

        # Identify number of features
        self.num_features = len(X[0])

        # Randomly choose centroids to begin with
        self.centroids = [X[i] for i in random.sample(range(len(X)), self.k)]

        # Perform iterative fitting
        current_itr     = 1
        while current_itr < self.max_iter:
            # Calculate distance between all points and centroid
            sample_distances = [[self.distance(sample, centroid) for centroid in self.centroids] for sample in X]

            # For each sample, find the closest centroid
            self.cluster_assignments = [distance.index(min(distance)) for distance in sample_distances]

            # Calculate new centroids using cluster assignments
            new_centroids = [None] * self.k
            for cluster in set(self.cluster_assignments):
                cluster_samples = [X[i] for i in range(len(X)) if self.cluster_assignments[i] == cluster]

                new_centroids[cluster] = [round(sum(cluster_samples[i][j] for i in range(len(cluster_samples)))/len(cluster_samples), self.precision) for j in range(self.num_features)]
    
            # Check to see if new centroids and old centroid match
            # and terminate execution if they do
            if self._stable(new_centroids):
                current_itr = self.max_iter

            # Update centroids
            self.centroids = new_centroids

            # Update iteration
            current_itr += 1

    def plot(self):
        # See if data are available for plotting
        if self.data is None:
            return 0
        
        # Visualize
        plt.figure()
        plt.scatter([data[0] for data in self.data], [data[1] for data in self.data], s = 100, c = self.cluster_assignments)
        plt.scatter([centroid[0] for centroid in self.centroids], [centroid[1] for centroid in self.centroids], c = 'k', marker = "x",  s = 500)
        plt.show()

    def predict(self, data):
        # See if new data is a single sample or not
        if isinstance(data[0], Iterable) and isinstance(data, Iterable):
            # Find the closest centroid for multiple samples
            centroid_distances = [[self.distance(sample, centroid) for centroid in self.centroids] for sample in data]
            return [distance.index(min(distance)) for distance in centroid_distances]
        else:
            # Find the closest centroid for single sample
            centroid_distances = [self.distance(data, centroid) for centroid in self.centroids]
            return centroid_distances.index(min(centroid_distances))

    def clusters(self):
        return self.cluster_assignments
    
    def centers(self):
        return self.centroids


# Main -------------------------------------------------------------------------
def main():
    # Initialize dataset
    X = [[x,y] for x,y in zip([11, 21, 28, 17, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53,
55, 61, 62, 70, 72, 10], [39, 36, 30, 52, 53, 46, 55, 59, 63, 70, 66, 63, 58, 23,
14, 8, 18, 7, 24, 10])]
    
    # Initialize KMeans
    kmeans = KMeans(k = 3)

    # Fit
    kmeans.fit(X)

    # Predict cluster assignment for new data
    new_data = [[20, 45],
                [30, 60],
                [50, 10],
                [70, 70],
                [55, 70],
                [65, 12]]
    new_data2 = [25, 25]

    print(kmeans.predict(new_data))
    print(kmeans.predict(new_data2))

    # Visualize
    kmeans.plot()


if __name__ == '__main__':
    main()