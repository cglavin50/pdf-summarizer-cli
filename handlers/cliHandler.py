import sys

helpText = 'This tool is used to extract text from a PDF and print/save it to a file.'
helpText += '\nCommand-Line args required: -f filePath\nOptional Command-Line args: -start startingPageNum -end endingPageNum -d dstFile'

def extractArgs():
    length = len(sys.argv)
    if length < 2:
        print(helpText)
        exit
    
    
    fileName = ''
    startPage = 0
    endPage = 0
    dstName = ''
    
    for i in range(1, length-1):
        if sys.argv[i] == '-f':
            fileName = sys.argv[i+1]
        if sys.argv[i] == '-start':
            startPage = int(sys.argv[i+1])
        if sys.argv[i] == '-end':
            endPage = int(sys.argv[i+1])
        if sys.argv[i] == '-d':
            dstName = sys.argv[i+1]
            
    
    if fileName == '':
        print("Error, no file path provided")
        exit
    
    return fileName, dstName, startPage, endPage
# extracts the required 
        