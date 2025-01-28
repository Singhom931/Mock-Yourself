import re
from tkinter import filedialog

def process_mock_test_content(content):
    global section_names , exam
    exam = content.partition("\n")[0]
    sections = ["Section"+sect for sect in content.split("Section") if sect ];  del sections[0] 
    section_names = [sect.partition("\n")[0] for sect in sections] 
    #questions = ["Question"+ques for sect in sections for ques in sect.split("Question") ]
    paperbysect = []
    sectbyques =[]
    for sect in sections:
        question = ["Question"+ques for ques in sect.split("Question") ];  del question[0]  ;sectbyques = []
        for ques in question:
            ques_opts = re.split(r":\n|\na\)|\nb\)|\nc\)|\nd\)|\nCorrect Answer:",ques);ques_opts.append(False); ques_opts.append(0); ques_opts.append(0)
            #print(ques_opts[-4])
            ques_opts[-4] = ques_opts[-4].strip();  ques_opts[-4] = ques_opts[-4][0]
            sectbyques.append(ques_opts)
        paperbysect.append(sectbyques)
    
    return paperbysect

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "D:\python\TestSeries Program\paper", title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    return filename

path = browseFiles()
print(path)
with open(path, "r") as file:
    content = file.read()

processed_data = process_mock_test_content(content)
section_names_only = [section.split(": ")[1] for section in section_names]

with open("paper/test.settings.txt", "r") as file:
    content = file.read()

settings = [setting.split('=')[1].strip() for setting in content.split('\n')]

sectperpaper = len(processed_data)
quespersect =  [len(sect) for sect in processed_data]

print(processed_data)

