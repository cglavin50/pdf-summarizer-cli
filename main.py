from handlers.cliHandler import extractArgs
from handlers.fileHandler import extractText
from handlers.modelHandler import summarizeText
from dotenv import load_dotenv
import time

# env initialization
load_dotenv('./.env', verbose=True)

def main():
    fileName, dst, startNum, endNum = extractArgs()
    text = extractText(fileName, startNum, endNum)
    
    start = time.time()
    summary = summarizeText(text)
    length = time.time() - start
    print("Summary written in", length, "seconds")
    if dst == "": # print to CLI
        print(summary, flush = True)
    else:
        file = open(dst, 'w')
        count = file.write(summary)
        if count == 0:
            raise Exception("Error, no text was found from the PDF provided. Exiting...")
        file.close()
    
    
main()