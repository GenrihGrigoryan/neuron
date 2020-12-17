import os

print(os.path)

path = ".neuron/output"

files = os.listdir(".neuron/output")

html = []

for file in files:
    if ".html" in file:
        html.append(file)

#print(html)

path += "/"

for hf in html:
    new_file_content = ""
    rf = open(path + str(hf), 'r')
    for line in rf:
        if '<h3 class="ui header">Backlinks</h3>' in line:
            new_file_content += line.replace('<h3 class="ui header">Backlinks</h3>', '<h3 class="ui header">Упоминания</h3>')
        #elif 'rel="canonical"' in  line:
        #    new_file_content += line.replace(".html", "")
        elif 'zettel-link' in  line:
            new_file_content += line.replace(".html", "")
        else:
            new_file_content += line
    rf.close()

    wf = open(path + str(hf), 'w')
    wf.write(new_file_content)
    wf.close()


