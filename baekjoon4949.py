class stack():
    def __init__(self):
        self.stack = []

    def push(self,n):
        self.stack.append(n)

    def pop(self):
        if len(self.stack) == 0:
            return False
        else:
            return self.stack.pop()

    def empty(self):
        if len(self.stack) == 0:
            return True
        else :
            return False

# chr_list = list(map(str, input().split('.')))
chr_list = []
while True:
    chr_nmb = input()
    if chr_nmb[0] == '.':
        break
    else :
        chr_list.append(chr_nmb)

while True :
    for check_list in chr_list:
        # print(check_list)
        # if check_list[0] == '.':
        #     break
        check_stack = stack()
        check = True
        for i in check_list:
            if i == '[' or i == '(':
                check_stack.push(i)
            elif i == ']':
                a = check_stack.pop()
                if a != '[' :
                    check = False
                    break
            elif i == ')':
                a = check_stack.pop()
                if a != '(':
                    check = False
                    break
        if check_stack.empty() == True and check == True:
            print('yes')
        else :
            print('no')
    break