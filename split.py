import numpy as np
'''
    X = training array
    y = testing array 

    This is to split the data into training and testing split using walk forward validation
    '''


class splitit():
    def split_sequences(sequences, n_steps_in, n_steps_out):
        X, y = list(), list()
        for i in range(len(sequences)):
            # find the end of this pattern
            end_ix = i + n_steps_in
            out_end_ix = end_ix + n_steps_out
            # check if we are beyond the dataset
            if out_end_ix > len(sequences):
                break
            # gather input and output parts of the pattern
            seq_x, seq_y = sequences[i:end_ix, :11], sequences[end_ix:out_end_ix, 10:11]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)
