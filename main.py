from kaggle_environments import make, evaluate, utils
from pprint import pprint
env1 = make("hungry_geese", debug=True) #set debug to True to see agent internals each step

env1.reset()
configuration = {"rows": 10, "columns": 8}
agents = ["./agent-astar.py","random","./enemies/submission-ralph-coward.py","./enemies/submission-ralph-coward.py"]
steps = env1.run(agents)



#pprint(steps)

with open('./game.html','wb') as f:   
    f.write(env1.render(mode="html",width=700, height=600).encode("UTF-8"))

