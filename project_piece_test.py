from board_square import BoardSquare, UrPiece

""" Feel free to change these constants to whatever your project constants are going to be"""
WHITE = 'White'
BLACK = 'Black'


def standard_board_move_test():
    piece = UrPiece(WHITE, 'W')
    bs_1 = BoardSquare(1, 1)
    bs_1.piece = piece
    piece.position = bs_1

    print("=" * 10 + "Test Unobstructed Move" + "=" * 10)

    bs_2 = BoardSquare(1, 2)
    bs_3 = BoardSquare(1, 3)
    bs_4 = BoardSquare(1, 4)
    bs_5 = BoardSquare(1, 5)
    bs_1.next_white = bs_2

    if piece.can_move(1):
        print('One move test successful.')
    else:
        print('One move test failed.')

    bs_2.next_white = bs_3

    if piece.can_move(2):
        print('Two move test successful.')
    else:
        print('Two move test failed.')

    bs_3.next_white = bs_4

    if piece.can_move(3):
        print('Three move test successful.')
    else:
        print('Three move test failed.')

    bs_4.next_white = bs_5

    if piece.can_move(4):
        print('Four move test successful.')
    else:
        print('Four move test failed.')


def standard_board_non_move_test():
    print("=" * 10 + "Test Landing on Piece of Same Color" + "=" * 10)
    piece = UrPiece(WHITE, 'W')
    bs_1 = BoardSquare(1, 1)
    bs_1.piece = piece
    piece.position = bs_1

    bs_2 = BoardSquare(1, 2)
    bs_3 = BoardSquare(1, 3)
    bs_4 = BoardSquare(1, 4)
    bs_5 = BoardSquare(1, 5)
    bs_1.next_white = bs_2
    bs_2.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(1):
        print('One move test successful.')
    else:
        print('One move test failed.')

    bs_2.next_white = bs_3
    bs_3.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(2):
        print('Two move test successful.')
    else:
        print('Two move test failed.')

    bs_3.next_white = bs_4
    bs_4.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(3):
        print('Three move test successful.')
    else:
        print('Three move test failed.')

    bs_4.next_white = bs_5
    bs_5.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(4):
        print('Four move test successful.')
    else:
        print('Four move test failed.')


def board_entrance():
    print("=" * 10 + "Board Entrance Test" + "=" * 10)
    piece = UrPiece(WHITE, 'W')
    bs_1 = BoardSquare(1, 1)
    bs_1.piece = piece
    piece.position = bs_1

    bs_2 = BoardSquare(1, 2)
    bs_3 = BoardSquare(1, 3)
    bs_4 = BoardSquare(1, 4)
    bs_5 = BoardSquare(1, 5)
    bs_1.next_white = bs_2
    bs_2.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(1):
        print('One move test successful.')
    else:
        print('One move test failed.')

    bs_2.next_white = bs_3
    bs_3.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(2):
        print('Two move test successful.')
    else:
        print('Two move test failed.')

    bs_3.next_white = bs_4
    bs_4.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(3):
        print('Three move test successful.')
    else:
        print('Three move test failed.')

    bs_4.next_white = bs_5
    bs_5.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(4):
        print('Four move test successful.')
    else:
        print('Four move test failed.')


def board_exit():
    print("=" * 10 + "Board Exit Test" + "=" * 10)
    piece = UrPiece(WHITE, 'W')
    bs_1 = BoardSquare(1, 1)
    bs_1.piece = piece
    piece.position = bs_1

    bs_2 = BoardSquare(1, 2)
    bs_3 = BoardSquare(1, 3)
    bs_4 = BoardSquare(1, 4)
    bs_5 = BoardSquare(1, 5)
    bs_1.next_white = bs_2
    bs_2.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(1):
        print('One move test successful.')
    else:
        print('One move test failed.')

    bs_2.next_white = bs_3
    bs_3.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(2):
        print('Two move test successful.')
    else:
        print('Two move test failed.')

    bs_3.next_white = bs_4
    bs_4.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(3):
        print('Three move test successful.')
    else:
        print('Three move test failed.')

    bs_4.next_white = bs_5
    bs_5.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(4):
        print('Four move test successful.')
    else:
        print('Four move test failed.')


def capture_test():
    print("=" * 10 + "Capture Test" + "=" * 10)
    piece = UrPiece(WHITE, 'W')
    bs_1 = BoardSquare(1, 1)
    bs_1.piece = piece
    piece.position = bs_1

    bs_2 = BoardSquare(1, 2)
    bs_3 = BoardSquare(1, 3)
    bs_4 = BoardSquare(1, 4)
    bs_5 = BoardSquare(1, 5)
    bs_1.next_white = bs_2
    bs_2.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(1):
        print('One move test successful.')
    else:
        print('One move test failed.')

    bs_2.next_white = bs_3
    bs_3.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(2):
        print('Two move test successful.')
    else:
        print('Two move test failed.')

    bs_3.next_white = bs_4
    bs_4.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(3):
        print('Three move test successful.')
    else:
        print('Three move test failed.')

    bs_4.next_white = bs_5
    bs_5.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(4):
        print('Four move test successful.')
    else:
        print('Four move test failed.')


def rosette_test():
    print("=" * 10 + "Rosette Test" + "=" * 10)
    piece = UrPiece(WHITE, 'W')
    bs_1 = BoardSquare(1, 1)
    bs_1.piece = piece
    piece.position = bs_1

    bs_2 = BoardSquare(1, 2)
    bs_3 = BoardSquare(1, 3)
    bs_4 = BoardSquare(1, 4)
    bs_5 = BoardSquare(1, 5)
    bs_1.next_white = bs_2
    bs_2.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(1):
        print('One move test successful.')
    else:
        print('One move test failed.')

    bs_2.next_white = bs_3
    bs_3.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(2):
        print('Two move test successful.')
    else:
        print('Two move test failed.')

    bs_3.next_white = bs_4
    bs_4.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(3):
        print('Three move test successful.')
    else:
        print('Three move test failed.')

    bs_4.next_white = bs_5
    bs_5.piece = UrPiece(WHITE, 'W2')

    if piece.can_move(4):
        print('Four move test successful.')
    else:
        print('Four move test failed.')

standard_board_move_test()
standard_board_non_move_test()
board_entrance()
board_exit()
capture_test()
rosette_test()