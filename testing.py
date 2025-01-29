import pandas as pd


def entropy(D):
    return 0

def Gain(D,A):
    return entropy(D) - entropy_A(D,A)
'''
function selectSplittingAttribute(A,D,threshold);
information gain p0 := enthropy(D); 
for each Ai ∈ Ado p[Ai] := enthropyAi (D);
   Gain[Ai] = p0−p[Ai]; 
//compute info gain endfor 
best := arg(findMax(Gain[])); 
if Gain[best] >threshold then return best else return NULL;
'''

def selectSplittingAttribute(A,D,threshold):
    p_0 = entropy(D)
    Gain = list()
    for i in A:
        Gain[i]=p_0 - entropy(i)
    best = index(Max(Gain))
    if Gain[best] > threshold:
        return best
    else:
        return NULL 
    
def selectSplittingAttribute2(A,D,threshold):
    p_0 = entropy(D)
    Gain = list()
    gainRatio = list()
    for i in A:
        a_ent = entropy(i)
        Gain[i]=p_0 - entropy(i)
        gainRatio[i]= Gain[i]/a_ent
    best = index(Max(gainRatio))
    if Gain[best] > threshold:
        return best
    else:
        return NULL 


def main():
    df = pd.read_csv('balloon.csv')
    print(df)


main()