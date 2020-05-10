def rotate_m(mat):
    a1 = ['','','','']
    for i in mat:
        m = -1
        for j in i:
            m += 1
            a1[m] = j + a1[m]
    
    return a1
 
def recall_password(template, cipher):
    password = ''
    for n in range (0, 4):
        for i in range(0, 4):
            for j in range(0,4):
                if template[i][j] == 'X':
                    password += cipher[i][j]
        template = rotate_m(template)
      
    return password