import hpptx 

print("Ahoj")

r= hpptx.get("https://example.com")
print(r.text)
lines = r.text.split("n")

for line in lines:
    if "EUR" in line :
        row = line 

        print(row)