# Imports
import numpy as np
from numpy import random

# Class
class Classifier:

    # Constructor
    def __init__(self, data, K):
        # Initalize Constants
        self.data = data
        self.K = K

        # Initialize variables
        self.centroid_locs = self.initialize_centroids()
        self.point_cluster_idx = [None for i in range(len(data))]

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

    # Reassign Cluster to each point
    def reassign_clusters(self):
        # Loop over datapoints
        for i in range(len(self.data)):
            p = self.data[i]
            # Find index of closest centroid
            min_dist, idx_min = np.inf, None
            for j, centroid in enumerate(self.centroid_locs):
                dist = self.eucladian(p, centroid)
                if dist < min_dist:
                    min_dist = dist
                    idx_min = j
            # Assign closest cluster to point
            self.point_cluster_idx[i] = idx_min


    # Eucladian Distance Between Two Points
    def eucladian(self, p1, p2):
        return np.sqrt(sum((p1 - p2) ** 2))

    # Relocate Centroids to average positions
    def relocate_centroids(self):
        # Loop over Centroids
        for c in range(self.K):
            sum = np.zeros_like(self.data[0])
            total = 0
            # Loop Over Data
            for i, point in enumerate(self.data):
                # If point belongs to centroid cluster
                if self.point_cluster_idx[i] == c:
                    sum += point
                    total += 1
            # Recalculate Center
            new_center_loc = sum / total
            # Reassign Center
            self.centroid_locs[c] = new_center_loc


# RUN FILE
if __name__ == '__main__':
    # Import File
    points = np.loadtxt('points.txt').reshape((60, 2, 1))

    # Initialize Classifier
    classifier = Classifier(points, 3)

    for i in range(100):
        classifier.reassign_clusters()
        classifier.relocate_centroids()
    print(classifier.point_cluster_idx)