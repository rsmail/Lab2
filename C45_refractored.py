import numpy as np
import pandas as pd

def preprocess_data(data, attr_values):
    for attr, values in attr_values.items():
        if values == ["continuous"]:
            data[attr] = pd.to_numeric(data[attr], errors='coerce')
    return data

def entropy(series):
    probs = series.value_counts(normalize=True).values
    return -np.sum(probs * np.log2(probs), where=probs > 0)

def information_gain(data, attribute, target):
    total_entropy = entropy(data[target])
    counts = data[attribute].value_counts(normalize=True).values
    entropies = data.groupby(attribute)[target].apply(entropy).values
    return total_entropy - np.sum(counts * entropies)

def best_split(data, attributes, target):
    gains = {attr: information_gain(data, attr, target) for attr in attributes}
    return max(gains, key=gains.get) 


def build_tree(data, attributes, target):
    unique_classes = data[target].unique()
    if len(unique_classes) == 1:
        return unique_classes[0]
    if not attributes:
        return data[target].mode().iloc[0]
    
    best_attr = best_split(data, attributes, target)
    tree = {best_attr: {}}
    for val, subset in data.groupby(best_attr):
        tree[best_attr][val] = build_tree(subset.drop(columns=[best_attr]), attributes - {best_attr}, target)
    return tree


def predict(tree, sample):
    if not isinstance(tree, dict):
        return tree 
    
    attr = next(iter(tree))  
    value = sample[attr]  
    
    if value in tree[attr]: 
        return predict(tree[attr][value], sample)
    else:
        return "Unknown"  





url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
columns = ["class", "cap-shape", "cap-surface", "cap-color", "bruises", "odor",
           "gill-attachment", "gill-spacing", "gill-size", "gill-color", "stalk-shape",
           "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring",
           "stalk-color-above-ring", "stalk-color-below-ring", "veil-type",
           "veil-color", "ring-number", "ring-type", "spore-print-color",
           "population", "habitat"]

df = pd.read_csv(url, names=columns)
df = df.head(500)
df





attributes = set(df.columns) - {"class"}  
target = "class"




tree = build_tree(df, attributes, target)
print(tree)



# Example of a single row (data point) as a dictionary
single_row = {
    'cap-shape': 'x',  # x for convex cap shape
    'cap-surface': 'f',  # f for smooth cap surface
    'cap-color': 'b',  # b for brown cap color
    'bruises': 't',  # t for bruises
    'odor': 'a',  # a for almond odor
    'gill-attachment': 'f',  # f for free gill attachment
    'gill-spacing': 'c',  # c for close gill spacing
    'gill-size': 'n',  # n for narrow gill size
    'gill-color': 'k',  # k for black gill color
    'stalk-shape': 'e',  # e for equal stalk shape
    'stalk-root': 'b',  # b for bulbous stalk root
    'stalk-surface-above-ring': 's',  # s for smooth stalk surface above ring
    'stalk-surface-below-ring': 's',  # s for smooth stalk surface below ring
    'stalk-color-above-ring': 'w',  # w for white stalk color above ring
    'stalk-color-below-ring': 'w',  # w for white stalk color below ring
    'veil-type': 'p',  # p for partial veil type
    'veil-color': 'w',  # w for white veil color
    'ring-number': 't',  # t for one ring
    'ring-type': 'e',  # e for evanescent ring type
    'spore-print-color': 'k',  # k for black spore print color
    'population': 's',  # s for scattered population
    'habitat': 'g',  # g for grassy habitat
}

# Assuming your decision tree is named `tree`
prediction = predict(tree, single_row)
print(f"Predicted class: {prediction}")