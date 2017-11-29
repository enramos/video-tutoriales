import os
import sys
import re
import fileinput

mds = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.md'):
            mds.append(file)

print(mds)

for file in mds:
    tmp_file = str(file) + '1'
    file_name = str(file)
    with open(file) as infile, open(tmp_file, 'w') as outfile:
        for line in infile:
            if 'https://www.youtube.com' in line and '(https://www.youtube.com' not in line:
                youtubeString = re.findall(r'^https.*youtube\S*', line)
                print(youtubeString)
                wholeLine = '{% youtube %}' + youtubeString[0] + '{% endyoutube %}'
                print(wholeLine)
                line = re.sub(r'https.*youtube\S*', wholeLine, line)
            outfile.write(line)
    infile.close()
    outfile.close()
    os.remove(file)
    os.rename(tmp_file, file_name)

# http://pythontesting.net/python/regex-search-replace-examples/#in_python