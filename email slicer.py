email = input('Enter your email adress: ').split()
#for the input leave a space between the @ and the username and domain
username = email[ :email.index('@')]
domain= email[email.index('@')+1:]

print('Your username is', ''.join(username), 'and your domain is', ''.join(domain))

