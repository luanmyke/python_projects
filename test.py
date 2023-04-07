board = ['-'] * 9  
fmtstr = ''.join(board)
fmtstr = "\n".join(fmtstr[i:i+3] for i in range(0, len(fmtstr), 3))
print(fmtstr)