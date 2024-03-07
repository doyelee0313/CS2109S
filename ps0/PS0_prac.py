def transpose_matrix(A):
    """
    Returns a new matrix that is the transpose of matrix A.
    """
    # TODO: add your solution here and remove `raise NotImplementedError`
    
    row = len(A)
    col = len(A[0])

    for i in range(col):
        for j in range(row):
            result[i][j] = 0 

    # for i in range(col)
    #     for j in range(row)            
    #         result[i][j] = A[j][i]

    return result