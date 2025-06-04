# 期中作業：系統程式相關專題 / 報告


## 主題：Mini 語言直譯器（Interpreter for MiniGo）
在先前學習 Terraform 時，因為需要使用 Go 語言（Golang）撰寫與擴充模組，因此接觸了 Go 的語法與執行架構。這讓我對其簡潔且結構清晰的語法印象深刻。

內容運用Chatgpt在[cpython](https://github.com/python/cpython/tree/main)的專案中尋找重點，分為三大類。
ChatGPT 協助下建立了直譯器的初始模板，包含三大核心模組：
1. **詞法分析（token）**  
2. **語法分析（AST, Abstract Syntax Tree）**  
3. **語意執行（Interpreter）**
透過實作這三個階段，我更深入理解了語言處理器的工作流程與 Go 語言的結構。

本設計並實作一個語法近似 Go 語言的簡易直譯器，具備以下功能：
- 支援 `var` 宣告與基本運算（+ - * /）
- 控制結構包含 `if`, `else`, `do while`
- 可列印運算結果（如 `print(x)`）
- 具備詞法分析（Lexer）、語法分析（Parser）與直譯器（Interpreter）

透過Chatgpt建立的基礎模板進行擴充
在此架構上，我進一步擴充了語言的語法與執行邏輯，並補上變數、控制結構與布林邏輯等基礎特性，讓語言具備最基本的運算與流程控制能力。
我定義並處理了以下關鍵字與語意：
```go
KEYWORDS = {"var", "if", "else", "while", "func", "return", "print", "true", "false"}
```

### 核心模組
- `lexer.c`：負責將原始碼字串轉換為 token。
- `parser.c`：建構 AST。
- `interpreter.c`：執行 AST。
- `main.c`：整合測試與執行流程。

### 示範範例
```go
var x = 10
var y = 20
if (x < y) {
    print("x is less than y")
} else {
    print("x is not less than y")
}
var i = 0
while (i < 3) {
    print(i)
    i = i + 1
}
```
