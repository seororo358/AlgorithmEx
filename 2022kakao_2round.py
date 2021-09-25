import json
import requests
import random


def renew_grade(user, win, lose, time):
    score = (40-time) * 99000 * 35 // 100000
    user[win] += score
    user[lose] = max(user[lose] - score, 0)

    print("renew")

def define_match(user, wait):
    pair = []
    while len(wait) > 1:
        f = wait.pop()
        t = wait.pop()
        pair.append([f[0], t[0]])
    print("define")

    return pair

def Gameresultapi(url,headers):
    path = 'game_result'
    res = []
    req = requests.get(url+'/'+path, headers = headers)
    j = req.json()
    for w, l, time in [(i['win'], i['lose'], i['taken']) for i in j['game_result']]:
        res.append((w, l, time))

    return res


def Waitingapi(url, headers):
    path = 'waiting_line'

    arr = []
    req = requests.get(url+'/'+path, headers=headers)
    j = req.json()

    for id, fr in [(i['id'], i['from']) for i in j['waiting_line']]:
        arr.append((id, fr))

    return arr


def Userinfoapi(url, headers, users):
    path = 'user_info'

    req = requests.get(url+'/'+path, headers=headers)
    j = req.json()
    for id, grade in [(i['id'], i['grade']) for i in j['user_info']]:
        users[id] = grade

    return users


#data = {'pairs':[[],,,,,]}

def Matchapi(url, headers, data):
    path = 'match'

    req = requests.put(url + '/' + path, headers=headers, data=data)
    j = req.json()

    return j


#data = [{'id': 1, 'grade': 1900},,,,,,]

def Changegradeapi(url, headers, data):
    path = 'change_grade'

    req = requests.put(url + '/' + path, headers=headers, data=data)
    j = req.json()

    return j


def main(qid):
    url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
    token = '90c097a3819eef80cdfd5c594b3c0fc1'
    path = 'start'
    headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    param = {'problem': qid}

    if qid == 1:
        count = 30
        mean = 1
    else:
        count = 900
        mean = 45

    user = [int(random.uniform(0, 9999)) for _ in range(count+1)]
    #playing = [0 for _ in range(count+1)]


    req = requests.post(url + '/' + path, headers=headers, data=json.dumps(param))
    js = req.json()
    auth_key = js['auth_key']
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}


    for i in range(596):
        user = Userinfoapi(url, headers=headers, users=user)
        if i < 555:
            wait_q = []
            wait_q = Waitingapi(url, headers=headers)

            pair = define_match(user, wait_q)
            js = Matchapi(url, headers=headers, data=json.dumps({'pairs': pair}))
            print(js['time'])
        res = Gameresultapi(url, headers=headers)
        commands = []
        while res and len(commands) <= 10:
            w, l, t = res.pop()
            renew_grade(user, w, l, t)
            commands.append({'id': w, 'grade': user[w]})
            commands.append({'id': l, 'grade': user[l]})

        js = Changegradeapi(url, headers=headers, data=json.dumps({'commands': commands}))
        print(js['status'])
        if js['status'] == "finished":
            break

    req = requests.post(url + '/' + path, headers=headers, data=json.dumps(param))
    js = req.json()

    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}

    req = requests.get(url+'/score', headers=headers)
    print(req.json()['score'])

main(1)
#main(2)