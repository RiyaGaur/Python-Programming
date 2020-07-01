from collections import OrderedDict 
def merge_the_tools(string, k):
    # your code goes here
    n=len(string)
    out = [(string[i:i+k]) for i in range(0, len(string), k)] 
    def removeDupWithOrder(str): 
        return "".join(OrderedDict.fromkeys(str)) 
    for i in out:
        i=removeDupWithOrder(i)
        print(i)
