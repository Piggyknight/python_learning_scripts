'''
test each func to easy debug
'''
import copy_right_generator
import export_word

'''
# unit test for StripCsFile
clines = copy_right_generator.StripCsFile("d:\\Project\\Git\\python_learning_scripts\\copy_right\\test.cs")
for line in clines:
    print(line)

# unit test for SearchCsFiles
lines = copy_right_generator.SearchCsFiles("f:\\Preforce\\Client\\trunk\\Assets\\3rdPlugins\\")
for line in lines:
    print(line)

#export_word.Export("test.doc", clines, "Calibri", 11)

'''

copy_right_generator.GeneratorWord("f:\\Preforce\\Client\\trunk\\Assets\\", 3500, 11)









