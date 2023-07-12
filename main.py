from handlers.cliHandler import extractArgs
from handlers.pdfHandler import extractText
from handlers.chatGPTHandler import summarizeText
from dotenv import load_dotenv

# env initialization
load_dotenv('./.env', verbose=True)

def main():
    fileName, dst, startNum, endNum = extractArgs()
    text = extractText(fileName, startNum, endNum)
    summary = summarizeText(text)
    summary = text
    if dst == "": # print to CLI
        print(summary, flush = True)
    else:
        file = open(dst, 'w')
        count = file.write(summary)
        if count == 0:
            raise Exception("Error, no text was found from the PDF provided. Exiting...")
        file.close()
    
    
main()