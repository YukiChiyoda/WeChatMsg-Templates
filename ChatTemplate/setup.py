with open('style.css', 'r', encoding='utf-8') as f:
    style = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    script = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    index = f.read()

label = 'const chatMessages = [\n/*注意看这是分割线*/\n];\n'

index = index.replace("<link rel=\"stylesheet\" href=\"style.css\">", "<style>\n" + style + "\n</style>")
index = index.replace("<script src=\"data.js\"></script>", "<script>\n" + label + "\n</script>")
index = index.replace("<script src=\"script.js\"></script>", "<script>\n" + script + "\n</script>")

print(index)

with open('template.html', 'w', encoding='utf-8') as f:
    print(f.write(index))