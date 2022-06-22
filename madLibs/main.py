from ready_madLibs import fun_park, zoo
import random
if __name__ == '__main__':
    obj = random.choice([fun_park, zoo])
    result = obj.madlibs()
    print(result)
