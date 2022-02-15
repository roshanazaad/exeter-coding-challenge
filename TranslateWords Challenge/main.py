
import time
import os
import psutil 


begin = time.time()


kv = {}
kvf = {}
translatedText = []

with open("find_words.txt","r") as file:
    for line in file:
       kv[line.strip()] = ""
      
with open("french_dictionary.csv","r") as file:
    for line in file:
        words = line.strip().split(",")
        if words[0] in kv:
           kv[words[0]] = words[1]

with open("t8.shakespeare.txt", "r") as file:
    for line in file:
        # breaking into words
        words = line.strip().split(" ")
        translatedWords = []

        for word in words:
            if word in kv:
                translatedWords.append(kv[word])
                if word in kvf:
                    kvf[word]+=1
                else:
                    kvf[word]=1    
            else:
                translatedWords.append(word)                    

        translatedLine = " ".join(translatedWords)
        translatedText.append(translatedLine)
# write translatedText to file (process)
with open("t8.shakespeare.translated.txt","w") as file:
    for line in translatedText:
        file.write(line+"\n")

with open("frequency.csv","w") as file:
    for word in kvf:
        file.write("%s,%s,%s\n"%(word,kv[word],kvf[word]))        

with open("unique.txt","w") as file:
    for word in kvf:
        file.write(word+"\n")

end = time.time()
print("Memory Used:", psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
print(f"Time to process : {end - begin}")


    