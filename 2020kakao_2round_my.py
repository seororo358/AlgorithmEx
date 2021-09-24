import json
import requests

scom = ['not', 'up', 'right', 'down', 'left', 'in', 'out']
dr = [0, -1, 0, 1, 0, 0, 0]
dc = [0, 0, 1, 0, -1, 0, 0]
tcommand = {scom[i]: i for i in range(7)}


class truck:
    def __init__(self):
        self.pos = 0
        self.load = 0


def getloc(url, headers, bycycle):
    path = 'locations'

    req = requests.get(url+'/'+path, headers=headers)
    j = req.json()

    for id, cnt in [(i['id'], i['located_bikes_count'])for i in j['locations']]:
        bycycle[id] = cnt

    return bycycle


def gettrucks(url, headers, trucks):
    path = 'trucks'

    req = requests.get(url+'/'+path, headers=headers)
    j = req.json()

    for id, loc, load in [(i['id'],i['location_id'],i['loaded_bikes_count'])for i in j['trucks']]:
        trucks[id].pos = loc
        trucks[id].load = load

    return trucks


def simulate(url, headers, command):
    path = 'simulate'

    req = requests.put(url+'/'+path, headers=headers, data=command)

    return req.json()


def truckmove(trucks, bicycles, mean, des, command):
    recom = []

    return recom


def getdist(loc, f, t):
    num = abs(loc[f][0] - loc[t][0]) + abs(loc[f][1] - loc[t][1])

    return num


def truckpath(loc, f, t):
    dcom = [tcommand['up'] for i in range(abs(loc[f][0] - loc[t][0])) if loc[f][0] > loc[t][0]]
    dcom.extend([tcommand['down'] for i in range(abs(loc[f][0] - loc[t][0])) if loc[f][0] < loc[t][0]])
    dcom.extend([tcommand['right'] for i in range(abs(loc[f][1] - loc[t][1])) if loc[f][1] < loc[t][1]])
    dcom.extend([tcommand['left'] for i in range(abs(loc[f][1] - loc[t][1])) if loc[f][1] > loc[t][1]])
    return dcom


def main(qid):
    URL = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users'
    token = '40183910509330daf1b31650b8aff7bb'
    path = 'start'
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    param = {'problem': qid}

    req = requests.post(URL+'/'+path, headers=headers, data=json.dumps(param))
    js = req.json()
    auth_key = js['auth_key']
    headers = {'Authorization': auth_key, 'Content-type': 'applications/json'}

    if qid == 1:
        msize = 5
        mean = 2
        truck_num = 5
        bnum = 4
    else:
        msize = 60
        mean = 3
        truck_num = 10
        bnum = 3

    by_map = [[msize-i-1 + msize*j] for j in range(msize) for i in range(msize)]
    pos = {by_map[i][j]: (i, j) for i in range(msize) for j in range(msize)}

    bycycles = [0 for _ in range(msize*msize)]
    trucks = [truck() for _ in range(truck_num)]

    truck_des = [0 for _ in range(len(trucks))]

    for time in range(720):
        bycycles = getloc(URL, headers=headers, bycycle=bycycles)
        emergen = [i[0] for i in enumerate(bycycles) if i[1] == 0 or i[1] > bnum]

        for e in emergen:
            minn = 10000
            for j in range(len(trucks)):
                if getdist(pos, trucks[j].pos, e) < minn:
                    truck_des[j] = e

        nextcom = []

        for i in range(truck_num):
            t = trucks[i]
            ncom = truckmove(t,bycycles,mean,truck_des[i])
            nextcom.append({'truck_id': i, 'command': ncom})

        j = simulate(URL, headers=headers, command=json.dumps({'commands': nextcom}))
        print(j['time'], j['failed_requests_count'])


    req = requests.get(URL+'/score', headers=headers)
    print(req.json()['score'])


main(1)
