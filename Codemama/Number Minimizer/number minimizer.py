def minimize_number(S, K):
    num_list = list(S)
    
    changes = 0

    for i in range(0,len(num_list)):
        if changes < K:
            if i == 0 and num_list[i] != '1':
                num_list[i] = '1'
                changes += 1
            elif i > 0 and num_list[i] != '0':
                num_list[i] = '0'
                changes += 1

    minimized_number = ''.join(num_list)
    
    print("Min =", minimized_number)


S, K = input().split()
K = int(K)
minimize_number(S,K)
