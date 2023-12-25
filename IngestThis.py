# Create a file called "ingest_this.txt"
# type the following in:
# This script Is completely awesome Like professor chaja

def replaceVowels(test_str, H):
	vowels = 'AEIOUaeiou'

	for k in vowels:
		test_str = test_str.replace(k, H)

	return test_str


input_str = input("Enter text: ")
H = "7"
print(replaceVowels(input_str, H))

# This script is completely awesome like professor chaja
