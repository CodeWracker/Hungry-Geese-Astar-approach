from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration,Action, row_col
from kaggle_environments.envs.hungry_geese.hungry_geese import adjacent_positions,min_distance
from pprint import pprint
import numpy as np
import pandas as pd
from math import *

ralph_last_action = [
    None,
    None,
    None,
    None
]
def get_grid_from_obs(obs,columns,rows):
    # 0: Livre
    # 1: Cabeça
    # 2: "Parede" (inimigos ou a ultima posicao)
    # 3: Comida (Objetivo)

        global ralph_last_action
        player_index = obs.index
        last_pos = ralph_last_action[player_index]
        mapa = []
        row = []
        for i in range(0,rows):
            mapa.append([])

            for j in range(0,columns):
                achou = False
                
                for food in obs['food']:
                    x,y = row_col(food,columns)
                    if(x == i and y == j):
                        mapa[i].append(3)
                        achou = True
                        break
                if(achou):
                    continue
                if(last_pos):
                    if(last_pos[0] == i and last_pos[1] == j):
                        mapa[i].append(2)
                        continue
                for goose in obs['geese']:
                    gs = 2
                    for part in goose:
                        x,y = row_col(part,columns)
                        if(x == i and y == j):
                            if(gs == 1 and last_pos == ralph_last_action[player_index]):
                                ralph_last_action[player_index] = [i,j]
                            mapa[i].append(gs)
                            achou = True
                            break
                    if(achou):
                        break
                if(achou):
                    continue
                mapa[i].append(0)
        return np.array(mapa)

def border_distance(p,lim):
    d = 0
    if(lim/2 < p):
        d = lim - p
    else:
        d = p
    return d
def distance(x1,y1,x2,y2,cols,rows):
    d1 = sqrt((x1-x2)**2)
    d2 = sqrt((y1-y2)**2)

    dx1 = border_distance(x1, rows)
    dx2 = border_distance(x2, rows)

    
    dy1 = border_distance(y1, cols)
    dy2 = border_distance(y2, cols)
    
    if(dx1+dx2<d1):
        d1 = dx1+dx2
    if(dy1+dy2<d2):
        d2 = dy1+dy2

    return  d1 + d2
def heristic(mapa,obs,columns,rows):
    heu = []
    foodPos = []
    for food in obs['food']:
        x,y = row_col(food,columns)
        foodPos.append([x,y])

    for i in range(0,mapa.shape[0]):
        
        heu.append([])
        for j in range(0,mapa.shape[1]):
            tp = mapa[i][j]
            if(tp == 2):
                heu[i].append(-1)
                continue
            else:
                d = 1000000
                for pos in foodPos:
                    if(d>distance(i, j, pos[0], pos[1],columns,rows)):
                        d = distance(i, j, pos[0], pos[1],columns,rows)
                heu[i].append(d)

    return np.array(heu,dtype="int32")
def agent(obs_dict,config_dict):
    global ralph_last_action
    
    #np.set_printoptions(precision=2)
    observation = Observation(obs_dict)
    configuration = Configuration(config_dict)
    mapa = (get_grid_from_obs(observation,configuration.columns,configuration.rows))
    #pprint(mapa)
    #pprint("")
    heuristic_map = heristic(mapa,observation,configuration.columns,configuration.rows)
    for line in heuristic_map:
        print(str(line).replace('\n', '') )
    print()
    print()
    '''
    state = get_grid_from_obs(obs,config.columns,config.rows)
    state = np.reshape(state, [1, nS])
    action =np.argmax(dqn.model.predict(state)) 
    actL = []
    for act in Action:
            actL.append(act)
    '''
    return "WEST"