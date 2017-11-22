'''
1. search "*.cs" through given folder including the child folder.
2. loop to read cs file, remove comment & space and cat links all of them
3. stop when we got 60 * 50 line of code (including the {}) hahahahah
4. using py-docx to create a word file and input the string
5. the word template rule is 
    - superscript with project name & page num from 1 - 100
    - the word format should be Calibri , num 5 
'''
import os
import export_word

def _end_with(s, *endstring):
    '''
    :param s: string to search 
    :param endstring: a list of search pattern
    :return: return true if contains any pattern in *endstring, else return false 
    '''
    array = map(s.endswith, endstring)
    if True in array:
        return True
    else:
        return False

def SearchCsFiles(rootFolder):
    '''
    search all cs files under given folder     
    '''
    result = list()
    for rt, dirs, files in os.walk(rootFolder):
        for f in files:
            if _end_with(f, '.cs'):
                result.append(os.path.join(rt,f))
    return result


def StripCsFile(filePath):
    '''
    :param filePath: absolute path for the cs file 
    :returns: return cs file string whihc has the space & comment lines stripped 
    '''
    try:
        result = list()
        for line in open(filePath, 'r', encoding='utf-8'):
            if not len(line.strip()) or line.strip().startswith("//"):
                continue
            result.append(line)
    except:
        print("error loading file", filePath)

    return result

def GeneratorWord(rootFolder, codeNum, fileNum):
    '''
    given certain folder to cat link all the cs and export to word doc 
    :return: 
    '''
    filePaths = SearchCsFiles(rootFolder)
    all_codes = list()
    fileCount = 1
    word_base_name = "copy_right_"
    print("Starting generation....")
    for file in filePaths:
        print("......collecting " + file)
        codes = StripCsFile(file)
        all_codes.extend(codes)
        # export word file if we collect enough lines of code
        if len(all_codes) > codeNum:
            word_file = "d:\\" + word_base_name + str(fileCount) + ".doc"
            print("export " + word_file)
            export_word.Export(word_file, all_codes,"Calibri", 11)
            fileCount += 1
            all_codes.clear()

        if fileCount > fileNum:
            break
    return



