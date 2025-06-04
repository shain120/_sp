## 習題 1: 請為下列編譯器加上 do while 迴圈的處理程式
[習題 1](https://github.com/shain120/_sp/tree/main/hw1)

老師提供的簡易編譯器加上 `do while` 迴圈的語法與處理邏輯。本題為老師的原檔擴充，其餘程式碼為原始教材。
- 修改 parser，加入 `do while`
- 先執行一次區塊，再判斷是否繼續。
```c
do {
    print(x);
    x = x - 1;
} while (x > 0);
```
## 習題 2 : c4 組合語言理解與硬塞練習
[習題 2](https://github.com/shain120/_sp/tree/main/hw2)
理解 c4 編譯器所產生的組合語言格式
使用 c4 編譯 `power2.c`，觀察產生的組合語言指令。
## 習題 3 : 請為 c4 編譯器加上 do while 迴圈
[習題 3](https://github.com/shain120/_sp/tree/main/hw3)
作業要求增加的功能為參考chatgpt，其餘為老師的原檔
延續 c4 編譯器架構，實作 `do while` 控制結構，需支援完整語法與正確執行，確保迴圈至少執行一次。

## 習題4: 寫一個組合語言程式，可以計算三個數相乘 (記得最後要印出結果）
[習題 4](https://github.com/shain120/_sp/tree/main/hw4)
撰寫組合語言程式以計算 a * b * c，並將結果輸出至終端機。
使用組合語言撰寫 `mul3` 函數，計算三個整數的乘積。
- 呼叫 `mul3` 並印出結果。
  ```bash
  gcc -std=c99 mul3main.c mul3.s
  ./a.out
  ```
## 習題5: 寫一個 C 語言的程式，然後用 gcc 與 objdump 做出下列結果
利用 `gcc` 編譯與 `objdump` 工具觀察對應的組合語言
[習題 5](https://github.com/shain120/_sp/tree/main/hw5)
原創，產生power(2,3)
- 使用 `gcc -S` 產生組合語言。
- 使用 `gcc -c` 編譯為目的檔。
- 使用 `objdump -d` 對目的檔進行反組譯。
- 使用 `objdump -h` 查看目的檔的表頭資訊。

## 期中作業：請寫一個系統程式相關的專案或報告
[期中](https://github.com/shain120/_sp/tree/main/mid)
[課程筆記](https://github.com/shain120/_sp/blob/main/系統程式學習筆記.pdf)
