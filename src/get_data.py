from ucimlrepo import fetch_ucirepo
import pandas as pd

def fetch_and_save():
    iris = fetch_ucirepo(id=53)
    X = iris.data.features
    y = iris.data.targets
    df = pd.concat([X, y], axis=1)
    df.to_csv("../data/raw/iris.csv", index=False)
    print("Saved Iris dataset to data/raw/iris.csv")

if __name__ == "__main__":
    fetch_and_save()


# from ucimlrepo import fetch_ucirepo 
  
# # fetch dataset 
# iris = fetch_ucirepo(id=53) 
  
# # data (as pandas dataframes) 
# X = iris.data.features 
# y = iris.data.targets 
  
# # metadata 
# print(iris.metadata) 
  
# # variable information 
# print(iris.variables) 
