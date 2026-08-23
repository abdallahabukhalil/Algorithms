def FindGCD(X: int, Y: int):
    if Y == 0 or X == 0: return X # need to fix, problems in inputing 0

    else:
        if X > Y: return FindGCD(Y, X % Y)

        else: return FindGCD(X, Y % X)

print(FindGCD(3, 26))