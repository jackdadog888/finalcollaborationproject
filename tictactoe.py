from tictactoeclass import TicTacToeFunctions


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1Letter, player2Letter = TicTacToeFunctions.inputplayer1Letter()
    turn = TicTacToeFunctions.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Player 1':
            # player 1's turn.
            TicTacToeFunctions.drawBoard(theBoard)
            move = TicTacToeFunctions.getplayer1Move(theBoard)
            TicTacToeFunctions.makeMove(theBoard, player1Letter, move)
            TicTacToeFunctions.drawBoard(theBoard)

            if TicTacToeFunctions.isWinner(theBoard, player1Letter):
                TicTacToeFunctions.drawBoard(theBoard)
                print('Hooray! Player 1 won the game!')
                gameIsPlaying = False
            else:
                if TicTacToeFunctions.isBoardFull(theBoard):
                    TicTacToeFunctions.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # player 2's turn.
            move = TicTacToeFunctions.getplayer2Move(theBoard)
            TicTacToeFunctions.makeMove(theBoard, player2Letter, move)

            if TicTacToeFunctions.isWinner(theBoard, player2Letter):
                TicTacToeFunctions.drawBoard(theBoard)
                print('Hooray! Player 2 won the game!')
                gameIsPlaying = False
            else:
                if TicTacToeFunctions.isBoardFull(theBoard):
                    TicTacToeFunctions.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    if not TicTacToeFunctions.playAgain():
        break
