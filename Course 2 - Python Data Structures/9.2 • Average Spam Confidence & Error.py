# 7.2 | Write a program that prompts for a file name
# then opens that file and reads through the file looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and
# compute the average of those values and produce an output as shown below:
# Average spam confidence: 0.750718518519
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

file_prompt = raw_input("Write the file name: ")  # 9-data.txt
try:
    file = open(file_prompt)
except:
    print "Error opening the file."
    exit()

vault = []

count_line = 0

for line in file:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence"):
        count_line = count_line + 1

        first_number = line.find("0")
        whole_number = line[first_number:]
        result = float(whole_number)

        vault.append(result)

output = sum(vault) / count_line

print "Average spam confidence:", output