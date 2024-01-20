import base64

admin = b"admin"

for i in range(0, 20):
		admin = base64.b64encode(admin)
		        
admin = admin.decode('utf-8')

admin.replace("1", "!")
admin.replace("2", "@")
admin.replace("3", "$")
admin.replace("4", "^")
admin.replace("5", "&")
admin.replace("6", "*")
admin.replace("7", "(")
admin.replace("8", ")")

print(admin)

nimda = b"nimda"

for i in range(0, 20):
		nimda = base64.b64encode(nimda)
		        
nimda = nimda.decode('utf-8')

nimda.replace("1", "!")
nimda.replace("2", "@")
nimda.replace("3", "$")
nimda.replace("4", "^")
nimda.replace("5", "&")
nimda.replace("6", "*")
nimda.replace("7", "(")
nimda.replace("8", ")")

print(nimda)