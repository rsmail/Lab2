import pandas as pd
import math



def entropy(C):

    val = C.unique()
    entropy = 0
    for i in val:
        Pr = C.value_counts()[i]/C.count()
        entropy = (Pr * math.log(Pr))
        return -entropy

'''
def entropy_Aj(D,C):

    val = D.unique()

    entropy = 0
    for i in val:
        Pr = C.value_counts()[i]/C.count()
        entropy = (Pr * math.log(Pr))
        return -entropy


def Gain(D,A):
    return entropy(D) - entropy_Aj(D,A)

function selectSplittingAttribute(A,D,threshold);
information gain p0 := enthropy(D); 
for each Ai ∈ Ado p[Ai] := enthropyAi (D);
   Gain[Ai] = p0−p[Ai]; 
//compute info gain endfor 
best := arg(findMax(Gain[])); 
if Gain[best] >threshold then return best else return NULL;
'''


def selectSplittingAttribute(df,target, threshold):
    C = df[target]
    D = df.loc[:,df.columns != target]
    D0 = entropy(C)
    Gain = {}

    for curr in D.columns:
       A=D[curr].unique()
       length = len(D)
       entAj = 0
       for i in A:
           Cj = C[D[curr] == i]
           S=len(Cj)
           entAj = entAj + S/length *entropy(Cj)
       Gain.update({curr:D0-entAj})
    if max(Gain.values()) >  threshold:
        return max(Gain, key=Gain.get)
    else:
        return None
    
def buildTree(df, target, threshold):
    best_split = selectSplittingAttribute(df,target,threshold)
    if best_split == None:
        print("No further splitting")
    else:
        edges = df[best_split].unique()

        splitD = list()
        for i in edges:
            splitD.append(df[df[best_split]==i].loc[:,df.columns != best_split])
        
        for data in splitD:
            print(data)
            buildTree(data, target, threshold)


def main():
    df = pd.read_csv('balloon.csv')
    target = 'Inflated'
    threshold = 0.05

    buildTree(df, target, threshold)

       


main()