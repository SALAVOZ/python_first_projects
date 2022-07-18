import time
from tqdm import tqdm
import requests
import csv
import aiohttp
import asyncio


async def http_get(urls):
    content = []
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in tqdm(urls, desc='Async fetching data...', colour='GREEN'):
            tasks.append(asyncio.create_task(session.get(url)))
        responses = await asyncio.gather(*tasks)
        return [await r.json() for r in responses]

def build_url(id):
    api = 'API.users.get({{\'user_ids\':{},\'fields\':\'occupation\'}})'.format(
        id * 25 + 1)
    for i in range(2, 26):
        api += ',API.users.get({{\'user_ids\':{},\'fields\':\'occupation\'}})'.format(
            id * 25 + i)
    url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(
        list_token[id % len(list_token)], api)
    return url


def run_case(func):
    #start_timestamp = time.time()
    requests_per_time = 15
    requests_to_do_again = []
    result = []
    for index in range(10_000, 1_000_000):#CURRENT_INDEX = 10_000  5 16700
        #time.sleep(3)
        print('index', index)
        result = []

        urls = [build_url(i) for i in range( index * requests_per_time, (index + 1) * requests_per_time )]

        found_people = asyncio.run(func(urls))
        try:
            for response in found_people:
                if 'error' in response:
                    requests_to_do_again.append('https://api.vk.com/method/execute?access_token=vk1.a.r6ggLUsQLrEZcBglCqNBMZky32j1e-olSz1872IzR3bDelipusqkgYJPh6lAtDCJBRm-bpmmNRtskXr4fwvM6SfrVBWhW08IJ98ORqnwoOE8-8HOR-ZDmoPwol4RsXX4gjTEdxQzawpzi93t4wmFdWdEQH85U17Y1vXishff9rlQSk-jkje7cOzY9psOQdAM&v=5.101&code=return%20' + response['error']['request_params'][1]['value'][7:])
                    continue
                for person in response['response']:
                    try:
                        if 'русал'.upper() in person[0]['occupation']['name'].upper():
                            result.append([f"{person[0]['first_name']} {person[0]['last_name']}", person[0]['id'], person[0]['occupation']['name']])
                    except:
                        continue
        except KeyError as ex:
            print('Strange Error')

        while requests_to_do_again:
            done = []
            for url in requests_to_do_again:
                r = requests.get(url).json()
                try:
                    for person in r['response']:
                        try:
                            if 'русал'.upper() in person[0]['occupation']['name'].upper():
                                result.append([f"{person[0]['first_name']} {person[0]['last_name']}", person[0]['id'], person[0]['occupation']['name']])
                        except KeyError as ex:
                            continue
                except TypeError as ex:
                    exit(0)
                except KeyError as ex:
                    time.sleep(1)
                    continue
                done.append(url)
                requests_to_do_again = [url for url in requests_to_do_again if url not in done]
        file = open("data.csv", 'a')
        for row in result:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(row)
    #task_time = round(time.time() - start_timestamp, 2)
    #rps = round(50 / task_time, 1)

#if __name__ == '__main__':
list_token = []
with open('tokens.txt', 'r') as f:
    for line in f:
        list_token.append(str(line).rstrip('\n'))
len(list_token)

#run_case(http_get)
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(run_case(http_get))