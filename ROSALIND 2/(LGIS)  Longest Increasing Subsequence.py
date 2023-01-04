def get_sequence(seq):
    if not seq:
        return seq

    lis = [None] * len(seq)    
    lds = [None] * len(seq)

    
    L = 1
    lis[0] = 0

    
    for i in range(1, len(seq)):
       
        lower = 0
        upper = L

        
        if seq[lis[upper-1]] < seq[i]:
            j = upper

        else:
            
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[lis[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower

        lds[i] = lis[j-1]

        if j == L or seq[i] < seq[lis[j]]:
            lis[j] = i
            L = max(L, j+1)

    
    result = []
    pos = lis[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = lds[pos]

    return result[::-1]    
if __name__ == "__main__":
    with open('rosalind_lgis.txt','r') as fid:
        n = int(fid.readline().strip())
        s = [int(x) for x in fid.readline().split()]
    fid.close() 
    #print s
    inc = get_sequence(s)
    dec = get_sequence(s[::-1])[::-1]
    fout = open('out.txt','w')
    fout.write('%s\n%s' %(str(inc).strip('[]').replace(',',''),str(dec).strip('[]').replace(',','')))
    fout.close()