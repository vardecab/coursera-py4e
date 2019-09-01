# 6.5 | Write code using find() and string slicing (see section 6.10)
# to extract the number at the end of the line below.
# Convert the extracted value to a floating point number and print it out.
# string: "X-DSPAM-Confidence:    0.8475"
# output: 0.8475

string = "X-DSPAM-Confidence:    0.8475"

first_number = string.find("0")
result = string[first_number:]
output = float(result)

print output