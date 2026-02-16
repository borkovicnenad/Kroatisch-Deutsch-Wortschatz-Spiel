import csv
import random
import time
from datetime import datetime
from termcolor import colored

class CSVRow: 
    def __init__(self, type, article, word, sufixes, croatian, example):
        self.type = type
        self.article = article
        self.word = word
        self.sufixes = sufixes
        self.croatian = croatian
        self.example = example
        
    def __repr__(self):
        return f"CSVRow({self.article}, {self.word}, {self.sufixes}, {self.example})"
    
def read_csv_to_objects(file_path):
    objects_list = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if len(row) >= 6:
                obj = CSVRow(row[0], row[1], row[2], row[3], row[4], row[5])
                objects_list.append(obj)
            else:
                print(f"Skipping row: {row} (not enough columns)")
    return objects_list

def append_to_file(file_name, input_data):
    try:
        with open(file_name, 'a') as file:
            file.write(input_data + '\n')
        print(f"Results successfully appended to {file_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
dictionary_file_path = './Wortschatz/Deutsch-B1-cpy.csv'
statistics_file_path = './Statistiken.csv'
dictionary_name = dictionary_file_path.split('/')[-1]
word_list = read_csv_to_objects(dictionary_file_path)
print(f"Hallo, Sie verwenden derzeit das {dictionary_name} Wörterbuch. Um das Spiel zu beenden, geben Sie „exit“ ein!")

finish = False
counter = 0
points = 0
start_time = time.time()
while not finish:
    current_word = random.choice(word_list)
    if current_word.article != '/':
        full_word = current_word.article + " " + current_word.word
    else:
        full_word = current_word.word

    user_input = input("\n" + current_word.croatian + ": ")
    
    if user_input.strip() == "exit":
        finish = True
    elif full_word.strip() == user_input.strip():
        points += 1
        counter += 1
        print(current_word.sufixes)
        print(colored('KORREKT!', 'green'))
        print(f"ERGEBNIS: {round(points/counter*100, 2)}%\n")
        print("............................................")
    else:   
        counter += 1 
        print (colored('FALSCH! ', 'red') + full_word.strip() + "'.")
        print(current_word.sufixes)
        print(f"RESULT: {round(points/counter*100, 2)}%\n")
        print("............................................")


end_time = time.time()
current_datetime = datetime.now()
total_time = end_time - start_time
formatted_time = time.strftime("%H:%M:%S", time.gmtime(total_time))
result = f"{current_datetime};{formatted_time};{dictionary_name};{points};{counter};{round(points/counter*100, 2)}"
print("===================================================================")
print(f"TIME: {formatted_time}")
print(f"RESULT: {points}/{counter} => {round(points/counter*100, 2)}%")

append_to_file(statistics_file_path, result)