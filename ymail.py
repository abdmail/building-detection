import yagmail


string1 = 'portal'

# opening a text file
file1 = open("ymail.txt", "r")

# read file content
readfile = file1.read()

# checking condition for string found or not
if string1 in readfile:
	sender_email = 'abdmail799@gmail.com'
	receiver_email = ['habhilash3@gmail.com','manikantar281@gmail.com']
	subject = "Check THIS out"
	sender_password ='L6JXLkAxnFxDiV4'

	yag = yagmail.SMTP(user=sender_email, password=sender_password)

	contents = ["This is the first paragraph in our email","As you can see, we can send a list of strings,","being this our third one",]

	attachments=['Desktop/File 1/image1.png','Desktop/File 1/gantt2.png','Desktop/File 1/gantt3.png']

	yag.send(receiver_email, subject, contents, attachments)

else:
	print('No Government Land Records Found in the area.')

# closing a file
file1.close()

