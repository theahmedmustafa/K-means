# Imports
import numpy as np

# Class
class Classifier:

    # Constructor
    def __init__(self, data, K):
        # Initalize Constants
        self.data = data
        self.K = K

        # Initialize variables
        self.centroid_locs = self.initialize_centroids()
        self.point_cluster_idx = []
        self.cluster_population = []

    # Initialize Centroid Locations
    def initialize_centroids(self):
        # Initalize List
        locs = []
        # Randomize Location from Data
        while len(locs) < self.K:
            idx = np.random.randint(0, len(self.data))
            loc = self.data[idx]
            if any(all(i == loc) for i in locs): continue
            locs.append(loc)
        # Return Locations
        return locs

    # Calculate 
    def reassign_clusters():
        pass


# RUN FILE
if __name__ == '__main__':
    # Import File
    points = np.loadtxt('points.txt').reshape((60, 2, 1))

    # Initialize Classifier
    classifier = Classifier(points, 3)

    