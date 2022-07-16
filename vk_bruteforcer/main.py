'''
import asyncio
from aiohttp import ClientSession
import json
import nest_asyncio
nest_asyncio.apply()
'''

import requests
import csv

list_token=[]
with open('tokens.txt', 'r') as f:
    for line in f:
        list_token.append(str(line).rstrip('\n'))
len(list_token)

def build_url(id):
    api = 'API.users.get({{\'user_ids\':{},\'fields\':\'city\'}})'.format(
        id * 25 + 1)
    for i in range(2, 26):
        api += ',API.users.get({{\'user_ids\':{},\'fields\':\'occupation\'}})'.format(
            id * 25 + i)
    url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(
        list_token[id % len(list_token)], api)
    return url

index = 0
result = []

for i in range(1_000_000_000):
    try:
        people = requests.get(build_url(i)).json()['response']
    except:
        exit(0)

    for person in people:
        try:
            if 'РУСАЛ' in person[0]['occupation']['name'].upper():
                result.append([f"{person[0]['first_name']} {person[0]['last_name']}", person[0]['id'], person[0]['occupation']['name']])
        except:
            continue

    print('checked: ', i * 25)
    print('found: ', len(result))
    if len(result) % 50 == 0 and len(result) != 0:
        with open(f'data{index}.csv', 'a') as file:
            for row in result:
                writer = csv.writer(file, delimiter=";")
                writer.writerow(row)
        index += 1



























'''
async def bound_fetch_zero(sem, id, session):
    async with sem:
        await fetch_zero(id, session)


async def fetch_zero(id, session):
    url = build_url(id)
    try:
        async with session.get(url) as response:

            # Считываем json
            resp = await response.text()
            js = json.loads(resp)
            list_users = [x for x in js['response'] if x != False]

            # Проверяем если город=1(Москва) тогда добавляем в лист
            for it in list_users:
                try:
                    if 'РУСАЛ' in it[0]['occupation']['name'].upper():
                        list_data.append([f"it[0]['last_name'] it[0]['first_name']", it[0]['id'], it[0]['occupation']['name']])
                except Exception:
                    pass

    except Exception as ex:
        print(f'Error: {js}')


#  Генерация url к апи вк, 25 запросов в одном
def build_url(id):
    api = 'API.users.get({{\'user_ids\':{},\'fields\':\'occupation\'}})'.format(
        id * 25 + 1)
    for i in range(2, 26):
        api += ',API.users.get({{\'user_ids\':{},\'fields\':\'occupation\'}})'.format(
            id * 25 + i)
    url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(
        list_token[id % len(list_token)], api)
    return url


async def run_zero(id):
    tasks = []
    sem = asyncio.Semaphore(1000)

    async with ClientSession() as session:
        #  Значение 3200 зависит от вашего числа токенов
        for id in range((id - 1) * 5, id * 5):
            task = asyncio.ensure_future(bound_fetch_zero(sem, id, session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses
        del responses
        await session.close()


# Запускаем  сборщик
for i in range(0, 17):
    for id in range(i * 500 + 1, (i + 1) * 500 + 1):
        print(id)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(run_zero(id))

    # Сохраняем айдишники в файл на гугл диске и очищаем лист
    with open(f'data{i}.txt', 'w') as f:
        for item in list_data:
            f.write(f'{item}\n')
    exit(0)
    print(len(list_data))
    list_data.clear()
'''