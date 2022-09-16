#Marketing wants to know two things: 
#How many total requests have been made in the 6 months?
#How many total requests were made in the time period represented by the log?

#downloadUrl = "https://s3.amazonaws.com/tcmg476/http_access_log"
#eq = requests.get(downloadUrl)

#response = requests.get("https://s3.amazonaws.com/tcmg476/http_access_log")

#with open(r"TCMG412Lab3.txt", 'r') as fp:
	#lines = len(fp.readlines())
	#print('Total Number of lines:', lines)

file = open('TCMG412Lab3.txt','r')

word1 = 'Oct'
word2 = 'Sep'
combined = word1 and word2

words = ["Oct", "Sep"]
count=0
lines=file.readlines()
for line in lines:
    if any(word in line for word in words):
        count+=1 
print(count)
