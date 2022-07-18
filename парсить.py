import csv

file = open('job.txt', encoding='utf-8', mode='r')
text = file.read()
result = []
#sa = 0
persons = []
index = 0
index_url = 0
index_fio = 0
#nav.go(this, event);">
is_person = True
while text.find('nav.go(this', index) != -1:
    index = text.find('nav.go(this', index)
    person = ''
    url = ''
    # ИЩЕМ URL
    if is_person:
        while text[index] != 'o':
            index -= 1
        #print(text[index])
        while text[index] != "/":
            url += text[index]
            index -= 1
        url = url[::-1]
        
        # ИЩЕМ ЧЕЛОВЕКА
        while text[index] != '>':
            index += 1
            #print(text[index])
        while text[index] != '<':
            person += text[index]
            index += 1
        is_person = False
        result.append([person[1:], url[0: len(url) - 3]])
    else:
        is_person = True
        #sa += 1
        #if sa == 10:
            #exit()
print('result len = ', int(len(result) / 2))
for person in range(0, len(result)):
    if person % 2 != 0:
        persons.append(result[person])
#print(persons)
with open('vk_job2.csv', "a", newline="") as file:
    for person in persons:
        writer = csv.writer(file, delimiter=';')
        try:
            writer.writerow(person)
        except UnicodeEncodeError as ex:
            continue