import os

files = os.listdir()

html = []

for file in files:
    if ".html" in file:
        html.append(file)

#print(html)

for hf in html:
    new_file_content = ""
    rf = open(str(hf), 'r')
    for line in rf:
        if '<h3 class="ui header">Backlinks</h3>' in line:
            new_file_content += line.replace('<h3 class="ui header">Backlinks</h3>', '<h3 class="ui header">Упоминания</h3>')
        else:
            new_file_content += line
    rf.close()

    wf = open(str(hf), 'w+')
    wf.write(new_file_content)
    wf.close()


