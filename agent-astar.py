from kaggle_environments.envs.hungry_geese.hungry_geese import Observation, Configuration,Action, row_col
from kaggle_environments.envs.hungry_geese.hungry_geese import adjacent_positions,min_distance
from pprint import pprint
import numpy as np
import pandas as pd

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
        print(last_pos)
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
                aux = 0
                for goose in obs['geese']:
                    gs = 2
                    if(aux == player_index):
                        gs = 1
                    aux = aux +1
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
    
def agent(obs_dict,config_dict):
    global ralph_last_action
    observation = Observation(obs_dict)
    configuration = Configuration(config_dict)
    mapa = (get_grid_from_obs(observation,configuration.columns,configuration.rows))
    pprint(mapa)
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