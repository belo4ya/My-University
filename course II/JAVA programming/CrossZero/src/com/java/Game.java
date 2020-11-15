package com.java;

import java.util.Scanner;

public class Game {

    final char SIGN_X = 'X';
    final char SIGN_O = 'O';
    final char SIGN_EMPTY = ' ';
    private char current_sign = 'X';
    char[][] table;
    Scanner scanner;

    public Game(){
        scanner = new Scanner(System.in);
        table = new char[3][3];
        for(int i=0; i<3;i++){
            for(int j=0; j<3; j++){
                table[i][j] = SIGN_EMPTY;
            }
        }
    }

    public void game(){
        showTable();
        while(!checkWin()){
            System.out.printf("Ход игрока %s", (current_sign == SIGN_X) ? "ОДИН\n": "ДВА\n");
            boolean move = false;
            while(!move){
                move = checkMove();
            }
            showTable();
        }
        System.out.printf("Победа игрока %s", (current_sign == SIGN_O) ? "ОДИН\n": "ДВА\n");
    }

    private void showTable(){
        System.out.println("   |0|1|2|");
        for(int i=0;i<3;i++){
            System.out.printf("%s  |%s|%s|%s|\n", i,
                    table[i][0], table[i][1], table[i][2]);
        }
        System.out.println();
    }

    private boolean checkInputMove(int number){
        if(number>=0 && number<3){
            return true;
        }
        else{
            return false;
        }
    }

    private boolean checkMove(){
        int row, col;

        while(true){
            System.out.println("Введите номер строки");
            row = scanner.nextInt();
            if(checkInputMove(row))
                break;
        }
        while(true){
            System.out.println("Введите номер колонки");
            col = scanner.nextInt();
            if(checkInputMove(col))
                break;
        }
        boolean ret = table[row][col] == SIGN_EMPTY;
        if(ret){
            table[row][col] = current_sign;
            current_sign = current_sign == SIGN_X ? SIGN_O : SIGN_X;
        }
        return ret;


    }

    private boolean checkWin(){
        for(int i=0; i<3; i++){
            if(table[i][0] != SIGN_EMPTY && table[i][0] == table[i][1] && table[i][0] == table[i][2])
                return true;
            if(table[0][i] != SIGN_EMPTY && table[0][i] == table[1][i] && table[0][i] == table[2][i])
                return true;
        }
        if(table[0][0] != SIGN_EMPTY && table[1][1] == table[0][0] && table[2][2] == table[0][0])
            return true;
        if(table[0][2] != SIGN_EMPTY && table[1][1] == table[0][2] && table[2][0] == table[0][2])
            return true;
        return false;
    }

}