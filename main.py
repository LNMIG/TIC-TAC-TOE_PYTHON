##### Importaciones ######################################################################################
import time
import os
from random import randrange
##########################################################################################################

##### Limpiar Pantalla ###################################################################################
if os.name == "posix":
    limpiar = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    limpiar = "cls"
##########################################################################################################


##### Datos iniciales a usars ############################################################################
board = [[1,2,3],[4,'X',6],[7,8,9]]
##########################################################################################################


##### Funciones ##########################################################################################
def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.

    os.system(limpiar)

    B = board
    print(f'''
        ╔═══════════════════════╗
        ║   TIC-TAC-TOE  GAME   ║
        ╚═══════════════════════╝
                                 
        █▀▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀▀█
        █       █       █       █
        █   {str(B[0][0])}   █   {str(B[0][1])}   █   {str(B[0][2])}   █
        █       █       █       █
        █▀▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀▀█
        █       █       █       █
        █   {str(B[1][0])}   █   {str(B[1][1])}   █   {str(B[1][2])}   █
        █       █       █       █
        █▀▀▀▀▀▀▀█▀▀▀▀▀▀▀█▀▀▀▀▀▀▀█
        █       █       █       █
        █   {str(B[2][0])}   █   {str(B[2][1])}   █   {str(B[2][2])}   █
        █       █       █       █
        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    '''
    )


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            move = int(input('\nPor favor ingrese un número libre del tablero: '))
            if 1 <= move <= 9:
                aux = move - 1
                fila = aux // 3
                columna = aux % 3
            if board[fila][columna] not in ['O', 'X']:
                board[fila][columna] = 'O'
                break
            else:
                print('\nAl parecer ya está ocupado ese cuadro. Intenta nuevamente.')
                print('\nSi deseas terminar el juego presiona CTRL + C.')
                input()
                continue
        except:
            print('\nNo parece ser un valor válido. Intenta de nuevo.')
            print('\nSi deseas terminar el juego presiona CTRL + C.')
            input()
            continue


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    libre = [1 for i in range(3) for j in range(3) if board[i][j] not in ['O','X'] ]
    return libre


def victory_for(board):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    empatado = make_list_of_free_fields(board)

    lineas_O = [True for i in range(3) if board[i].count('O') == 3]
    lineas_X = [True for i in range(3) if board[i].count('X') == 3]
    columnas_O = [True for i in range(3) for j in range(1) if board[j][i] == board[j+1][i] == board[j+2][i] == 'O']
    columnas_X = [True for i in range(3) for j in range(1) if board[j][i] == board[j+1][i] == board[j+2][i] == 'X']
    cruz1_O =  [True if board[0][0] == board[1][1] == board[2][2] == 'O' else None]
    cruz2_O =  [True if board[0][2] == board[1][1] == board[2][0] == 'O' else None]
    cruz1_X =  [True if board[0][0] == board[1][1] == board[2][2] == 'X' else None]
    cruz2_X =  [True if board[0][2] == board[1][1] == board[2][0] == 'X' else None]

    estado_O = [lineas_O, columnas_O, cruz1_O, cruz2_O]
    estado_X = [lineas_X, columnas_X, cruz1_X, cruz2_X]

    for each in estado_O:
        if len(each) > 0 and each[0]:
          return 'usuario'
    for each in estado_X:
        if len(each) > 0 and each[0]:
          return 'programa'
    if len(empatado) == 0:
        return 'empate'
    return 'seguir'


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.

    while True:
        move = randrange(8)
        fila = move // 3
        columna = move % 3
        if board[fila][columna] not in ['O', 'X']:
            board[fila][columna] = 'X'
            break
        else:
            continue


##### Ciclo de ingreso del movimiento de tablero #########################################################
while True:

    display_board(board)
    resultado = victory_for(board)
    if resultado == 'seguir':
        display_board(board)
        enter_move(board)
        # display_board(board)
        draw_move(board)
        continue
    elif resultado == 'usuario':
        print('         ¡¡  El usuario gana  !!')
        break
    elif resultado == 'programa':
        print('         ¡¡  El programa gana !!')
        break
    else:
        print('      ¡¡ Nadie gana, nadie pierde !!')
        break
##########################################################################################################