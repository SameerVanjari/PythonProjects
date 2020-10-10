import requests
import pickle

def write_pickle(data_file, fil):
    with open(fil, 'wb') as fileobj:
        pickle.dump(data_file, fileobj)
    
def read_pickle(fil):
    with open(fil,'rb') as f:
       return pickle.load(f)

if __name__ == "__main__":
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = requests.get(url).text
    data = iris.splitlines()
    read =[[i] for i in data]
    # write_pickle(read,"irisDat.pkl")
    ar = read_pickle("irisDat.pkl")
    print(ar)