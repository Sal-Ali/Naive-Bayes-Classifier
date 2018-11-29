import inspect
import sys
import numpy as np
from collections import Counter
import math


k = 50
#laplace smoothing constant

'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)


'''
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit) 
'''
def extract_basic_features(digit_data, width, height):
    features=[False if digit_data[i][j] == 0 else True
              for i in range(height) for j in range(width)]
  #  _raise_not_defined()
    return features

'''
Extract advanced features that you will come up with 
'''
def extract_advanced_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    
    # + as 1 # as 2
    #only + is true
    # odds ratio of + to #
    _raise_not_defined()
    return features

'''
Extract the final features that you would like to use
'''
def extract_final_features(digit_data, width, height):
    features=[]
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    return extract_basic_features(digit_data, width, height)
    #_raise_not_defined()
    return features

'''
Compupte the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training. 
'''
def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0):
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    size = float(np.trunc(len(label) * percentage / 100))
    # size of training set
    label_count = Counter(label)
    #initiate counting of priors
    global priors
    priors = [np.divide(label_count.get(n) * percentage / 100, size)  for n in range(10)]
    #the priors


    
    global conditionals, conditional_count, false_count
    #global declaration
    conditional_count = [[k for x in range(width*height)] for c in range(10)]
    #empty pixel list
    for i in range(int(size)):
        image = data[i] # each image
        img_label = label[i] #each corresponding label
        features = feature_extractor(image, width, height) #features for each image, pixels
        count = label_count.get(img_label) #the number of times said digit shows up in training set
        conditional_count[img_label] += np.asarray(features) # adds all the trues
    false_count = [[ (float(count - x + 2 * k) / 5000) # label_count.get(c))
    #becomes the frequency of falses
    for x in conditional_count[c]] for c in range(10)]
    conditional_count = [[(float(x) / 5000) # label_count.get(c))
    #becomes the frequency of truths
    for x in conditional_count[c]] for c in range(10)]
    
    
    
    conditionals = []
    
    

    
    
        
        # number of times it takes value 'false'
    
    # list of data stored in list, feature extract each one by one
    #_raise_not_defined()

'''
For the given features for a single digit image, compute the class 
'''
def compute_class(features):
    size = len(features)
    values = [0 for r in range(10)]

    for i in range(10):
        true = conditional_count[i]
        false = false_count[i]
        for f in range(size):
            if features[f] == True:
                
                values[i] += np.log(true[f])
            if features[f] == False:
                
                values[i] += np.log(false[f])
        values[i] += math.log(priors[i])
    predicted = np.argmax(values)
    
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    #_raise_not_defined()
    return predicted

'''
Compute joint probaility for all the classes and make predictions for a list
of data
'''
def classify(data, width, height, feature_extractor):
    
    predicted=[compute_class(feature_extractor(image, width, height)) 
    for image in data]
    
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    #_raise_not_defined()

    return predicted







        
    
