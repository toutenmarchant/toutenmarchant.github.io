import re
import glob
import htmlmin

r = re.compile(r"(<body.*?>).*?(<meta)", re.DOTALL|re.MULTILINE)

print("ta mere")

for file in glob.glob('D:/.wor/container/20200613010316/*.html'):  # use any mask suitable for you
# for file in glob.glob('D:\\.wor\\test\\*.html'):  # use any mask suitable for you
    print(f"cleaning: {file}") # prints full file path

    with open(file, 'r', encoding="utf-8") as file_input:
        # full_array = file_input.readlines()
        # head = "".join(full_array[:80])
        # body = "".join(full_array[81:])
        filedata = file_input.read()

    # head_cleaned = r.sub(r"\1 \2", head)
    # filedata = head_cleaned + body

    filedata_mini = htmlmin.minify(filedata, remove_empty_space=True, remove_comments=True)
    # Write the file out again
    with open(file, 'w', encoding="utf-8") as file_output:
        file_output.write(filedata_mini)