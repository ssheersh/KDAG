import numpy as np

def pdf(mean, var, x):
    num = np.exp(-(x-mean)**2/(2*var))
    den = np.sqrt(2*np.pi*var)
    return num/den

class NaiveBayes():
    # init function not required

    def fit(self, X, y):
        n_samples, n_features = X.shape # type of X and y is numpy.ndarrays
        self._classes = np.unique(y)
        n_classes= len(self._classes)
        
        # init mean, var and prior for each class
        self._mean = np.zeros((n_classes, n_features), dtype=np.Float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.Float64)
        self._priors = np.zeros(n_classes, dtype=np.Float64)

        for idx, c in enumerate(self._classes):
            X_c = X[y==c]
            self._mean[idx, : ] = X_c.mean(axis=0)
            self._var[idx, : ] = X_c.var(axis=0)
            self._priors[idx] = X_c.shape[0] / float(n_samples)

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self, x):
        #Basically implementing the Bayes theorem here
        posteriors = []

        for idx,c in enumerate(self._classes):
            prior=np.log(self._priors[idx])
            posterior = np.sum(np.log(pdf(self._mean[idx],self._var[idx],x)))
            posterior = posterior + prior
            posteriors.append(posterior)

            return self._classes[np.argmax(posteriors)]
