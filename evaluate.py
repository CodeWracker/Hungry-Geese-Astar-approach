from kaggle_environments import make, evaluate, utils
from pprint import pprint
import matplotlib.pyplot as plt
from tqdm import tqdm
import plotly.express as px 
import pandas as pd

astarP = [0]
randP = [0]
cowardP = [0]
ind = [0]
for i in tqdm(range(0,1000)):
    env1 = make("hungry_geese", debug=False) #set debug to True to see agent internals each step
    env1.reset()
    configuration = {"rows": 10, "columns": 8}
    agents = ["./agent-astar.py","random","./enemies/submission-ralph-coward.py"]
    steps = env1.run(agents)

    obs = steps[len(steps) - 1][0]["observation"]
    astar = astarP[len(astarP)-1]
    rand = randP[len(randP)-1]
    coward = cowardP[len(cowardP)-1]
    geese = obs["geese"]
    if(len(geese[0])>0):
        astar = astar + 1
    if(len(geese[1])>0):
        rand = rand + 1
    if(len(geese[2])>0):
        coward = coward + 1
    
    astarP.append(astar)
    randP.append(rand)
    cowardP.append(coward)
    ind.append(len(ind))


df = pd.DataFrame()
df["astar"] = astarP
df["random"] = randP
df["coward"] = cowardP
df["ind"] = ind
fig = px.line(df, x='ind', y=['astar', 'random','coward'])
fig.show()
fig.write_html("plot.html")