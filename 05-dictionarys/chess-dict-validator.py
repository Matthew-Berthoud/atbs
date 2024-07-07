import pprint


def isValidChessBoard(d: dict) -> bool:
    valid_names = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    black_pieces = {}
    white_pieces = {}

    for tile, piece in d.items():
        color = piece[0]
        name = piece[1:]
        
        print(color, name)
        print(tile)


        if name not in valid_names:
            return False

        if tile[0] not in "12345678" or tile[1] not in "abcdefgh":
            return False

        if color == 'b':
            black_pieces.setdefault(name, 0)
            black_pieces[name] += 1
            black_pieces.setdefault("sum", 0)
            black_pieces["sum"] += 1

        elif color == 'w':
            white_pieces.setdefault(name, 0)
            white_pieces[name] += 1
            white_pieces.setdefault("sum", 0)
            white_pieces["sum"] += 1

        else:
            return False

    if black_pieces.get("king", 0) != 1 or white_pieces.get("king", 0) != 1:
        return False

    if black_pieces.get("sum", 0) not in range(1,16) or white_pieces.get("sum", 0) not in range(1,16):
        return False

    if black_pieces.get("pawn", 0) not in range(9) or white_pieces.get("pawn", 0) not in range(9):
        return False

    return True


board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

print(isValidChessBoard(board))

