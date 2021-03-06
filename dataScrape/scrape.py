def main():
    # reading and scrubbing a file form NASA
    source_file = "RealData.txt"
    target_file = "RealData_goodData.json"

    s = open(source_file, 'r')
    t = open(target_file, 'w')
    countRecords, countHeader = 0,0
    new_text = '['
    for line in s:
        new_line = ""
        currentLine = line.rstrip("\n")
        if (countHeader == 0):
            header = currentLine.split()
            countHeader += 1
        if (currentLine[:5] != "State"):
            values = currentLine.split()
            new_line += "{"
            new_line += "\"" + str(values[0]) + "\": {"
            for i in range (1, 6):
                new_line += '\"'+ str(header[i]) + "\""
                new_line += ": "
                new_line += "\"" + str(values[i]) + "\""
                if (i != 5):
                    new_line += ","
            if (currentLine[:7] == "Wyoming"):
                new_line += "}}\n"
            else:
                new_line += "}},\n"
        new_text += new_line
        countRecords += 1
    new_text += "]"
    t.write(new_text)

    s.close()
    t.close()
    print("File written. %d records. " % countRecords)
main()
