## main.cpp

產生組合語言.s檔
```
g++ -S main.cpp
```
執行power.cpp
```
g++ main.cpp
 ./a.exe
```
產生目的檔.o檔
```
g++ -c main.cpp
```
將該目的檔反組譯
```
objdump -d main.o
```
```sh
.\main.o:     file format pe-i386


Disassembly of section .text:

00000000 <__Z5powerii>:
   0:   55                      push   %ebp
   1:   89 e5                   mov    %esp,%ebp
   3:   83 ec 10                sub    $0x10,%esp
   6:   c7 45 fc 01 00 00 00    movl   $0x1,-0x4(%ebp)
   d:   c7 45 f8 00 00 00 00    movl   $0x0,-0x8(%ebp)
  14:   8b 45 f8                mov    -0x8(%ebp),%eax
  17:   3b 45 0c                cmp    0xc(%ebp),%eax
  1a:   7d 10                   jge    2c <__Z5powerii+0x2c>
  1c:   8b 45 fc                mov    -0x4(%ebp),%eax
  1f:   0f af 45 08             imul   0x8(%ebp),%eax
  23:   89 45 fc                mov    %eax,-0x4(%ebp)
  26:   83 45 f8 01             addl   $0x1,-0x8(%ebp)
  2a:   eb e8                   jmp    14 <__Z5powerii+0x14>
  2c:   8b 45 fc                mov    -0x4(%ebp),%eax
  2f:   c9                      leave  
  30:   c3                      ret

00000031 <_main>:
  31:   8d 4c 24 04             lea    0x4(%esp),%ecx
  35:   83 e4 f0                and    $0xfffffff0,%esp
  38:   ff 71 fc                pushl  -0x4(%ecx)
  3b:   55                      push   %ebp
  3c:   89 e5                   mov    %esp,%ebp
  3e:   53                      push   %ebx
  3f:   51                      push   %ecx
  40:   83 ec 10                sub    $0x10,%esp
  43:   e8 00 00 00 00          call   48 <_main+0x17>
  48:   c7 44 24 04 03 00 00    movl   $0x3,0x4(%esp)
  4f:   00
  50:   c7 04 24 05 00 00 00    movl   $0x5,(%esp)
  57:   e8 a4 ff ff ff          call   0 <__Z5powerii>
  5c:   89 c3                   mov    %eax,%ebx
  5e:   c7 44 24 04 01 00 00    movl   $0x1,0x4(%esp)
  65:   00
  66:   c7 04 24 00 00 00 00    movl   $0x0,(%esp)
  6d:   e8 00 00 00 00          call   72 <_main+0x41>
  72:   89 1c 24                mov    %ebx,(%esp)
  75:   89 c1                   mov    %eax,%ecx
  77:   e8 00 00 00 00          call   7c <_main+0x4b>
  7c:   83 ec 04                sub    $0x4,%esp
  7f:   b8 00 00 00 00          mov    $0x0,%eax
  84:   8d 65 f8                lea    -0x8(%ebp),%esp
  87:   59                      pop    %ecx
  88:   5b                      pop    %ebx
  89:   5d                      pop    %ebp
  8a:   8d 61 fc                lea    -0x4(%ecx),%esp
  8d:   c3                      ret

0000008e <___tcf_0>:
  8e:   55                      push   %ebp
  8f:   89 e5                   mov    %esp,%ebp
  91:   83 ec 08                sub    $0x8,%esp
  94:   b9 00 00 00 00          mov    $0x0,%ecx
  99:   e8 00 00 00 00          call   9e <___tcf_0+0x10>
  9e:   c9                      leave  
  9f:   c3                      ret

000000a0 <__Z41__static_initialization_and_destruction_0ii>:
  a0:   55                      push   %ebp
  a1:   89 e5                   mov    %esp,%ebp
  a3:   83 ec 18                sub    $0x18,%esp
  a6:   83 7d 08 01             cmpl   $0x1,0x8(%ebp)
  aa:   75 1f                   jne    cb <__Z41__static_initialization_and_destruction_0ii+0x2b>
  ac:   81 7d 0c ff ff 00 00    cmpl   $0xffff,0xc(%ebp)
  b3:   75 16                   jne    cb <__Z41__static_initialization_and_destruction_0ii+0x2b>
  b5:   b9 00 00 00 00          mov    $0x0,%ecx
  ba:   e8 00 00 00 00          call   bf <__Z41__static_initialization_and_destruction_0ii+0x1f>
  bf:   c7 04 24 8e 00 00 00    movl   $0x8e,(%esp)
  c6:   e8 00 00 00 00          call   cb <__Z41__static_initialization_and_destruction_0ii+0x2b>
  cb:   90                      nop
  cc:   c9                      leave  
  cd:   c3                      ret

000000ce <__GLOBAL__sub_I__Z5powerii>:
  ce:   55                      push   %ebp
  cf:   89 e5                   mov    %esp,%ebp
  d1:   83 ec 18                sub    $0x18,%esp
  d4:   c7 44 24 04 ff ff 00    movl   $0xffff,0x4(%esp)
  db:   00
  dc:   c7 04 24 01 00 00 00    movl   $0x1,(%esp)
  e3:   e8 b8 ff ff ff          call   a0 <__Z41__static_initialization_and_destruction_0ii>
  e8:   c9                      leave
  e9:   c3                      ret
  ea:   90                      nop
  eb:   90                      nop
```
印出該目的檔的表頭
```
objdump -h power.o
```
```sh
.\main.o:     file format pe-i386

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         000000ec  00000000  00000000  0000012c  2**2
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000000  00000000  00000000  00000000  2**2
                  ALLOC, LOAD, DATA
  2 .bss          00000004  00000000  00000000  00000000  2**2
                  ALLOC
  3 .rdata        0000000c  00000000  00000000  00000218  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .ctors        00000004  00000000  00000000  00000224  2**2
                  CONTENTS, ALLOC, LOAD, RELOC, DATA
  5 .rdata$zzz    00000024  00000000  00000000  00000228  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  6 .eh_frame     000000cc  00000000  00000000  0000024c  2**2
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, DATA
```
