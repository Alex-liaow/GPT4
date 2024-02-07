def split_text(file_path, output_path, line_length):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    lines = [text[i:i+line_length] for i in range(0,len(text),line_length)]

    with open(output_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')

# 這行應該放在最後
split_text('v1.txt', 'v2.txt', 300)