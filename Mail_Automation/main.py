REPLACE_WORD= "[name]"

with open("./Input File/Name List/NameList.txt") as name_file:
    file_name = name_file.readlines()

with open("./Input File/Letters/Letter.txt") as letter_file:
    text = letter_file.read()
    for name in file_name:
        final_name = name.strip()
        replaced_text = text.replace(REPLACE_WORD, final_name)

        with open(f"Output File/Ready to use/{final_name}_letter.txt", mode="w") as final_file:
            final_file.write(replaced_text)
