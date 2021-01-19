""" Created by minhnq """
import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    wordMatrix = {}
    for i in range(size_x):
        for j in range(size_y):
            wordMatrix[str(i) + ' ' + str(j)] = {'sub':[], 'ins':[], 'del':[]}

    for i in range(size_x):
        matrix [i, 0] = i
        if i != 0:
            ins = wordMatrix[str(i-1) + ' 0']['ins'].copy()
            ins.append(seq1[i-1]+ '-' + str(i-1))
            wordMatrix[str(i) + ' 0'] = {'sub':[], 'ins':ins, 'del':[]}
    for j in range(size_y):
        matrix [0, j] = j
        if j != 0:
            _del = wordMatrix['0 ' + str(j-1)]['del'].copy()
            _del.append(seq2[j-1]+ '-' + str(j-1))
            wordMatrix['0 ' + str(j)] = {'sub':[], 'ins':[], 'del':_del}

    for i in range(1, size_x):
        for j in range(1, size_y):
            if seq1[i-1] == seq2[j-1]:
                matrix [i,j] = min(
                    matrix[i-1, j] + 1,
                    matrix[i-1, j-1],
                    matrix[i, j-1] + 1
                )
                wordMatrix[str(i) + ' ' + str(j)] = wordMatrix[str(i-1) + ' ' + str(j-1)].copy()
            else:
                matrix[i, j] = min(
                    matrix[i - 1, j] + 1,
                    matrix[i - 1, j - 1]+1,
                    matrix[i, j - 1] + 1
                )
                if matrix[i,j] == matrix[i - 1, j] + 1:  # del
                    _del  = wordMatrix[str(i-1) +  ' ' + str(j)]['del'].copy()
                    ins  = wordMatrix[str(i-1) +  ' ' + str(j)]['ins'].copy()
                    sub  = wordMatrix[str(i-1) +  ' ' + str(j)]['sub'].copy()
                    _del.append(seq1[i-1]+ '-' + str(i-1))
                    wordMatrix[str(i)+ ' ' + str(j)] = {'sub': sub, 'ins':ins, 'del':_del}
                elif matrix[i,j] == matrix[i, j-1] + 1: # ins
                    ins = wordMatrix[str(i) + ' ' + str(j-1)]['ins'].copy()
                    sub = wordMatrix[str(i) + ' ' + str(j-1)]['sub'].copy()
                    _del = wordMatrix[str(i) + ' ' + str(j-1)]['del'].copy()
                    ins.append(seq2[j-1]+ '-' + str(j-1))
                    wordMatrix[str(i) + ' ' + str(j)] = {'sub': sub, 'ins':ins, 'del':_del}
                elif matrix[i,j] == matrix[i - 1, j - 1] + 1: # sub
                    sub = wordMatrix[str(i - 1) + ' ' + str(j-1)]['sub'].copy()
                    ins = wordMatrix[str(i - 1) + ' ' + str(j-1)]['ins'].copy()
                    _del = wordMatrix[str(i - 1) + ' ' + str(j-1)]['del'].copy()
                    sub.append(seq1[i-1] + '-' + str(i-1))
                    wordMatrix[str(i) + ' ' + str(j)] = {'sub': sub, 'ins':ins, 'del':_del}

    s1=[]
    s2=[]
    sys= []
    dict_err = wordMatrix[str(len(seq1)) + ' ' + str(len(seq2))]
    s = dict_err['sub']
    i = dict_err['ins']
    d = dict_err['del']
    err_by_index = {}
    err_by_index = dict(err_by_index, **{k.split('-')[1]:'S-' + k.split('-')[0] for k in s})
    err_by_index = dict(err_by_index, **{k.split('-')[1]:'I-' + k.split('-')[0] for k in i})
    err_by_index = dict(err_by_index, **{k.split('-')[1]:'D-' + k.split('-')[0] for k in d})
    count = 0
    for i in range(max(len(seq1), len(seq2))):
        if err_by_index.get(str(i), None) == None:
            s1.append(seq1[count])
            s2.append(seq2[count])
            sys.append('C')
        else:
            err_type, word = err_by_index[str(i)].split('-')
            sys.append(err_type)
            if err_type == 'S':
                s1.append(seq1[count])
                s2.append(seq2[count])
            elif err_type == 'D':
                s2.append('***')
                s1.append(seq1[count])
            elif err_type == 'I':
                s1.append('***')
                s2.append(seq2[count])
        count+=1

    print("Seq 1: " + ' '.join(s1))
    print("Seq 2: " + ' '.join(s2))
    print('Sys:   ' + ' '.join(sys))
    print('Min error: ' + str(int(matrix[size_x - 1, size_y - 1])))
    print("===========================")
    pass

levenshtein('sitting', 'kitten')
levenshtein('kitty', 'kitten')
levenshtein('sitting', 'fitting')

