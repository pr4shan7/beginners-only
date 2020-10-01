/*
Tic-Tac-Toe game in C
Tic-Tac-Toe game in C
Tic-Tac-Toe is a two player game where each player uses a signature.  The player who successfully places three respective signatures in a vertical, horizontal or diagonal row is the winner.

Step 1: Use 3 X 3 matrix to get 9 cell tic tac toe board.
Step 2: Signature 'X' is used for player 1 and 'Y' for player 2.  And the players play
           alternatively.
Step 3: Get index as input from the players.  And the index range is 1-9. i.e) from 
           cell 1 to cell 9.
Step 4: After each move, check whether that player has placed three respective
           signatures in vertical, horizontal or diagonal row.  If yes, declare that
           particular player as winner.
Step 5: If no, give chance for other player.
Step 6: If all the cells in the Tic-Tac-Toe board got filled, then the game is drawn.



*/


 #include <stdio.h>
  int main() {
        int winner = 0, count = 0;
        int data[9], index, sign, player, flag, i, k, j;

        for (i = 0; i < 9; i++)
                data[i] = ' ';

        while (count < 9) {
                flag = 0;
                system("clear");
                printf("\n\n");
                printf("\t\t\t  %c | %c  | %c  \n", data[0], data[1], data[2]);
                printf("\t\t\t----+----+----\n");
                printf("\t\t\t  %c | %c  | %c  \n", data[3], data[4], data[5]);
                printf("\t\t\t----+----+---\n");
                printf("\t\t\t  %c | %c  | %c  \n", data[6], data[7], data[8]);
                if (count % 2 == 0) {
                        sign = 'X';
                        player = 1;
                } else {
                        sign = 'Y';
                        player = 2;
                }
                printf("Move for player%d(1-9):", player);
                scanf("%d", &index);
                if (index < 1 || index > 9) {
                        printf("Allowed index is 1 to 9!!\n");
                        continue;
                }
                if (data[index - 1] == 'X' || data[index - 1] == 'Y') {
                        printf("Position Already occupied!!\n");
                        sleep(1);
                        continue;
                }
                data[index - 1] = sign;
                count++;

                for (i = 0; i < 9; i++) {
                        if (i % 3 == 0)
                                flag = 0;

                        if (data[i] == sign)
                                flag++;

                        if (flag == 3) {
                                winner = 1;
                                goto win;
                        }
                }

                flag = 0;
                for (i = 0; i < 3; i++) {
                        for (k = i; k <= i + 6; k = k + 3) {
                                if (data[k] == sign)
                                        flag++;
                        }
                        if (flag == 3) {
                                winner = 1;
                                goto win;
                        }
                        flag = 0;
                }
                if ((data[0] == sign && data[4] == sign && data[8] == sign) ||
                        (data[2] == sign && data[4] == sign && data[6] ==  sign)) {
                        winner = 1;
                        goto win;
                }
        }
  win:
        system("clear");
        printf("\n\n");
        printf("\t\t\t  %c | %c  | %c  \n", data[0], data[1], data[2]);
        printf("\t\t\t----+----+----\n");
        printf("\t\t\t  %c | %c  | %c  \n", data[3], data[4], data[5]);
        printf("\t\t\t----+----+---\n");
        printf("\t\t\t  %c | %c  | %c  \n\n", data[6], data[7], data[8]);
        if (winner) {
                printf("Player %d is the winner. Congrats!!\n", player);
        } else {
                printf("Match draw.. Best of luck for both\n");
        }
        return 0;
  }
