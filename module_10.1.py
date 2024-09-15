from time import sleep
import time
from threading import Thread

def write_words(word_count, file_name):
    range_ = range(word_count)
    file = open(file_name, 'a', encoding='utf-8')
    for i in range_:
        file.write(f"Какое-то слово № {i+1}"+'\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')



start = time.time()
ex1=write_words(10,'example1.txt')
ex2=write_words(30,'example2.txt')
ex3=write_words(200,'example3.txt')
ex4=write_words(100,'example4.txt')
finish = time.time()
res = finish - start
print(f'{res} сек')


thr_ex5 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_ex6= Thread(target=write_words, args=(30, 'example6.txt'))
thr_ex7 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_ex8 = Thread(target=write_words, args=(100, 'example8.txt'))


start = time.time()
thr_ex5.start()
thr_ex6.start()
thr_ex7.start()
thr_ex8.start()
thr_ex5.join()
thr_ex6.join()
thr_ex7.join()
thr_ex8.join()
finish = time.time()
res = finish - start
print(f'{res} сек')



