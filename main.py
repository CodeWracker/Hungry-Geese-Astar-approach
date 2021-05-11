import kaggle_environments
from kaggle_environments import make, evaluate, utils
from pprint import pprint
env1 = make("hungry_geese", debug=True) #set debug to True to see agent internals each step

env1.reset()
agents = ["./agent-astar.py","random","./enemies/submission-ralph-coward.py","./enemies/submission-ralph-coward.py"]
obs = env1.run(agents)



with open('./game.html','wb') as f:   
    f.write(env1.render(mode="html",width=700, height=600).encode("UTF-8"))

