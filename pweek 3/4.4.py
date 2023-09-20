def new_password(oldpassword, newpassword):
    return newpassword != oldpassword and len(newpassword) >= 6

print(new_password('hello', 'nndhdhhdhdo'))