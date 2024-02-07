import re

with open('時代華語2md檔/all.md', 'r', encoding='utf-8') as file:
    keywords = ["對 話", "## 生詞", "## 語法", "## 短文", "課室活動"]
    content = file.read()
    ch_patt = re.compile('(' + '|'.join(keywords) + ')((?:.|\n)*?)(?=' + '|'.join(keywords) + '|$)')

    file_count = 1
    matches = ch_patt.findall(content)
    for match in matches:
        for keyword in keywords:
            if keyword in match[0]: 
                new_content = match[0] + match[1]
                # 將所有空行（連續兩個換行符）改為換行字元
                new_content = new_content.replace("\n\n", "\n")
                with open(str(file_count) + '_' + keyword.replace(" ", "_").replace("#", "") + '.md', 'w', encoding='utf-8') as new_file:
                    new_file.write(new_content)
                    file_count += 1