import requests
import random
import csv
import argparse

'''
sex 
1 - woman
2 - man
0 - any

age_from and age_to
birth_year
1566
3474
'''


def get_token():
    list_token = []
    with open('tokens_alex.txt', 'r') as f:
        for line in f:
            list_token.append(str(line).rstrip('\n'))
    return random.choice(list_token)


def build_url_get_ids_50(job):
    urls_array = []
    for age in range(14, 100, 2):
        urls = []
        for i in range(0, 1000, 50):
            code = 'API.users.search({{\'company\':\'{}\',\'sex\':0,\'fields\':\'occupation\',\'age_from\':\'{}\',\'age_to\':\'{}\',\'count\':50,\'offset\':{}}})'.format(job, age, age + 1, i)
            url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(get_token(), code)
            urls.append(url)
        urls_array.append(urls)
    return urls_array

def build_url_get_ids(job, token, age):
    code = 'API.users.search({{\'company\':\'{}\',\'sex\':0,\'fields\':\'occupation\',\'age_from\':\'{}\',\'age_to\':\'{}\',\'count\':1000}})'.format(
        job, age, age + 1)
    url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(token, code)
    return url


def build_url_brute_users(ids):
    code = ''
    for id in ids:
        code += 'API.users.get({{\'user_ids\':\'{}\',\'fields\':\'occupation\'}}),'.format(id)
    code = code[0:-1]
    url = 'https://api.vk.com/method/execute?access_token={}&v=5.101&code=return%20[{}];'.format(get_token(), code)
    return url


def get_ids_by_age(job, ids_file_name):
    request_to_get_again = []
    urls = build_url_get_ids_50(job)
    for url_array in urls:
        for url in url_array:
            try:
                response = requests.get(url).json()['response'][0]
                if len(response['items']) == 0:
                    break
                count, people = response['count'], response['items']
                txt = open(ids_file_name, 'a')
                for person in people:
                    txt.write(str(person['id']) + '\n')
            except KeyError as exp:
                print('Error')
                request_to_get_again.append(url)
    while request_to_get_again:
        done = []
        for url in request_to_get_again:
            try:
                res = requests.get(url).json()['response'][0]
                people = res['items']
                txt = open(ids_file_name, 'a')
                for person in people:
                    txt.write(str(person['id']) + '\n')
                done.append(url)
            except KeyError:
                continue
        request_to_get_again = [url for url in request_to_get_again if url not in done]


def get_users_info(urls, csv_file_name):
    count = 0
    requests_to_get_again = []
    file = open(csv_file_name, 'a', newline='')
    for url in urls:
        try:
            result = []
            r = requests.get(url)
            people = r.json()['response']
            for person in people:
                try:
                    if person == []:
                        continue
                    print('found', person[0]['first_name'], person[0]['last_name'])
                    result.append([f"{person[0]['first_name']} {person[0]['last_name']}", person[0]['occupation']['name'], person[0]['id']])
                except IndexError:
                    print('here is error')
                    exit(0)
                except KeyError:
                    continue
            for row in result:
                try:
                    writer = csv.writer(file, delimiter=";")
                    writer.writerow(row)
                except UnicodeEncodeError as exp:
                    continue
                count += 1
        except KeyError as exp:
            requests_to_get_again.append(url)
    print('count of found users', count)
    print('let\'s do requests which returned with an error')
    while requests_to_get_again:
        done = []
        for url in requests_to_get_again:
            try:
                r = requests.get(url).json()
                people = r['response']
                for person in people:
                    print('found', person[0]['first_name'], person[0]['last_name'])
                    try:
                        result.append([f"{person[0]['first_name']} {person[0]['last_name']}", person[0]['occupation']['name'],person[0]['id']])
                    except KeyError:
                        continue
                for row in result:
                    writer = csv.writer(file, delimiter=";")
                    count += 1
                    writer.writerow(row)
                done.append(url)
            except KeyError:
                continue
        requests_to_get_again = [url for url in requests_to_get_again if url not in done]
    print('Count of all found users', count)


def parse_people(file_name_to_read, file_name_to_write_result, job):
    count = 2424
    current = 0
    with open(file_name_to_read, 'r') as file:
        with open(file_name_to_write_result, 'a', newline='') as file_result:
            reader = csv.reader(file)
            writer = csv.writer(file_result, delimiter=";")
            for i, line in enumerate(reader):
                if job.upper() in line[0].split(';')[1].upper():
                    writer.writerow(line[0].split(';'))
                current += 1
                print('{}/{}'.format(current, count))


def all_proccess(job, ids_file_name, cvs_file_name, cvs_result_file_name):
    get_ids_by_age(job, ids_file_name) # ЗАПИСАЛИ IDS В ФАЙЛ
    get_users_info(get_ids_from_ids_file(ids_file_name), cvs_file_name) # ЗАПИСАЛИ НАЙДЕННЫХ ПОЛЬЗОВАТЕЛЕЙ В CSV ФАЙЛ
    parse_people(cvs_file_name, cvs_result_file_name, job)

def get_ids_from_ids_file(ids_file_name):
    file = open(ids_file_name, 'r')
    urls = []
    ids = []
    line = 'not empty string'
    while line != '':
        line = file.readline()
        ids.append(line.replace('\n', ''))
        if len(ids) % 25 == 0:
            urls.append(build_url_brute_users(ids))
            print('loaded:', len(urls * 25))
            ids = []
    urls.append(build_url_brute_users(ids))
    return urls


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Write args: ')
    parser.add_argument('--job', type=str, required=True, help='Write job place')
    parser.add_argument('--ids_file', type=str)
    parser.add_argument('--age_file', type=str)
    parser.add_argument('--result_csv_file', type=str)
    parser.add_argument('--do', type=str)
    args = parser.parse_args()
    if args.do == 'all':
        all_proccess(args.job, args.ids_file, args.age_file ,args.result_csv_file)