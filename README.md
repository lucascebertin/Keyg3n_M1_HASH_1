# [Keyg3n_M1#1](https://crackmes.one/crackme/5e66aea233c5d4439bb2dde8)

Desafio simples (nivel 1) do site crackmes.one

Baixe o arquivo zipado e leia o FAQ para descobrir qual é a senha do zip.

Rode o arquivo keygen.py, receba uma key e coloque como input do keygen.bin ou, se preferir, redirecione o stdin do script em python para o executável através do comando abaixo:
```bash
./keygen.bin <<< $(python3 ./keygen.py)
```

## Pré-requisito:
- linux (ou algo compatível, foi feito e testando em um manjaro)
- python 3

## Informações sobre o binário:

```bash
$ file keygen.bin
./keygen.bin: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2ef368e97b5763a497e168b8a53ca6efb54ab8df, not stripped

$ readelf -a ./keygen.bin
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x6f0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          6712 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         9
  Size of section headers:           64 (bytes)
  Number of section headers:         29
  Section header string table index: 28

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         0000000000000238  00000238
       000000000000001c  0000000000000000   A       0     0     1
  [ 2] .note.ABI-tag     NOTE             0000000000000254  00000254
       0000000000000020  0000000000000000   A       0     0     4
  [ 3] .note.gnu.build-i NOTE             0000000000000274  00000274
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .gnu.hash         GNU_HASH         0000000000000298  00000298
       000000000000001c  0000000000000000   A       5     0     8
  [ 5] .dynsym           DYNSYM           00000000000002b8  000002b8
       0000000000000120  0000000000000018   A       6     1     8
  [ 6] .dynstr           STRTAB           00000000000003d8  000003d8
       00000000000000c9  0000000000000000   A       0     0     1
  [ 7] .gnu.version      VERSYM           00000000000004a2  000004a2
       0000000000000018  0000000000000002   A       5     0     2
  [ 8] .gnu.version_r    VERNEED          00000000000004c0  000004c0
       0000000000000040  0000000000000000   A       6     1     8
  [ 9] .rela.dyn         RELA             0000000000000500  00000500
       00000000000000c0  0000000000000018   A       5     0     8
  [10] .rela.plt         RELA             00000000000005c0  000005c0
       0000000000000090  0000000000000018  AI       5    22     8
  [11] .init             PROGBITS         0000000000000650  00000650
       0000000000000017  0000000000000000  AX       0     0     4
  [12] .plt              PROGBITS         0000000000000670  00000670
       0000000000000070  0000000000000010  AX       0     0     16
  [13] .plt.got          PROGBITS         00000000000006e0  000006e0
       0000000000000008  0000000000000008  AX       0     0     8
  [14] .text             PROGBITS         00000000000006f0  000006f0
       00000000000002c2  0000000000000000  AX       0     0     16
  [15] .fini             PROGBITS         00000000000009b4  000009b4
       0000000000000009  0000000000000000  AX       0     0     4
  [16] .rodata           PROGBITS         00000000000009c0  000009c0
       000000000000003a  0000000000000000   A       0     0     4
  [17] .eh_frame_hdr     PROGBITS         00000000000009fc  000009fc
       0000000000000044  0000000000000000   A       0     0     4
  [18] .eh_frame         PROGBITS         0000000000000a40  00000a40
       0000000000000130  0000000000000000   A       0     0     8
  [19] .init_array       INIT_ARRAY       0000000000200d90  00000d90
       0000000000000008  0000000000000008  WA       0     0     8
  [20] .fini_array       FINI_ARRAY       0000000000200d98  00000d98
       0000000000000008  0000000000000008  WA       0     0     8
  [21] .dynamic          DYNAMIC          0000000000200da0  00000da0
       00000000000001f0  0000000000000010  WA       6     0     8
  [22] .got              PROGBITS         0000000000200f90  00000f90
       0000000000000070  0000000000000008  WA       0     0     8
  [23] .data             PROGBITS         0000000000201000  00001000
       0000000000000010  0000000000000000  WA       0     0     8
  [24] .bss              NOBITS           0000000000201010  00001010
       0000000000000008  0000000000000000  WA       0     0     1
  [25] .comment          PROGBITS         0000000000000000  00001010
       000000000000002b  0000000000000001  MS       0     0     1
  [26] .symtab           SYMTAB           0000000000000000  00001040
       0000000000000678  0000000000000018          27    43     8
  [27] .strtab           STRTAB           0000000000000000  000016b8
       000000000000027e  0000000000000000           0     0     1
  [28] .shstrtab         STRTAB           0000000000000000  00001936
       00000000000000fe  0000000000000000           0     0     1
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), I (info),
  L (link order), O (extra OS processing required), G (group), T (TLS),
  C (compressed), x (unknown), o (OS specific), E (exclude),
  l (large), p (processor specific)

There are no section groups in this file.

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
  PHDR           0x0000000000000040 0x0000000000000040 0x0000000000000040
                 0x00000000000001f8 0x00000000000001f8  R      0x8
  INTERP         0x0000000000000238 0x0000000000000238 0x0000000000000238
                 0x000000000000001c 0x000000000000001c  R      0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000b70 0x0000000000000b70  R E    0x200000
  LOAD           0x0000000000000d90 0x0000000000200d90 0x0000000000200d90
                 0x0000000000000280 0x0000000000000288  RW     0x200000
  DYNAMIC        0x0000000000000da0 0x0000000000200da0 0x0000000000200da0
                 0x00000000000001f0 0x00000000000001f0  RW     0x8
  NOTE           0x0000000000000254 0x0000000000000254 0x0000000000000254
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_EH_FRAME   0x00000000000009fc 0x00000000000009fc 0x00000000000009fc
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     0x10
  GNU_RELRO      0x0000000000000d90 0x0000000000200d90 0x0000000000200d90
                 0x0000000000000270 0x0000000000000270  R      0x1

 Section to Segment mapping:
  Segment Sections...
   00     
   01     .interp 
   02     .interp .note.ABI-tag .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt .init .plt .plt.got .text .fini .rodata .eh_frame_hdr .eh_frame 
   03     .init_array .fini_array .dynamic .got .data .bss 
   04     .dynamic 
   05     .note.ABI-tag .note.gnu.build-id 
   06     .eh_frame_hdr 
   07     
   08     .init_array .fini_array .dynamic .got 

Dynamic section at offset 0xda0 contains 27 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000c (INIT)               0x650
 0x000000000000000d (FINI)               0x9b4
 0x0000000000000019 (INIT_ARRAY)         0x200d90
 0x000000000000001b (INIT_ARRAYSZ)       8 (bytes)
 0x000000000000001a (FINI_ARRAY)         0x200d98
 0x000000000000001c (FINI_ARRAYSZ)       8 (bytes)
 0x000000006ffffef5 (GNU_HASH)           0x298
 0x0000000000000005 (STRTAB)             0x3d8
 0x0000000000000006 (SYMTAB)             0x2b8
 0x000000000000000a (STRSZ)              201 (bytes)
 0x000000000000000b (SYMENT)             24 (bytes)
 0x0000000000000015 (DEBUG)              0x0
 0x0000000000000003 (PLTGOT)             0x200f90
 0x0000000000000002 (PLTRELSZ)           144 (bytes)
 0x0000000000000014 (PLTREL)             RELA
 0x0000000000000017 (JMPREL)             0x5c0
 0x0000000000000007 (RELA)               0x500
 0x0000000000000008 (RELASZ)             192 (bytes)
 0x0000000000000009 (RELAENT)            24 (bytes)
 0x000000000000001e (FLAGS)              BIND_NOW
 0x000000006ffffffb (FLAGS_1)            Flags: NOW PIE
 0x000000006ffffffe (VERNEED)            0x4c0
 0x000000006fffffff (VERNEEDNUM)         1
 0x000000006ffffff0 (VERSYM)             0x4a2
 0x000000006ffffff9 (RELACOUNT)          3
 0x0000000000000000 (NULL)               0x0

Relocation section '.rela.dyn' at offset 0x500 contains 8 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000200d90  000000000008 R_X86_64_RELATIVE                    7f0
000000200d98  000000000008 R_X86_64_RELATIVE                    7b0
000000201008  000000000008 R_X86_64_RELATIVE                    201008
000000200fd8  000100000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_deregisterTMClone + 0
000000200fe0  000600000006 R_X86_64_GLOB_DAT 0000000000000000 __libc_start_main@GLIBC_2.2.5 + 0
000000200fe8  000700000006 R_X86_64_GLOB_DAT 0000000000000000 __gmon_start__ + 0
000000200ff0  000a00000006 R_X86_64_GLOB_DAT 0000000000000000 _ITM_registerTMCloneTa + 0
000000200ff8  000b00000006 R_X86_64_GLOB_DAT 0000000000000000 __cxa_finalize@GLIBC_2.2.5 + 0

Relocation section '.rela.plt' at offset 0x5c0 contains 6 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000200fa8  000200000007 R_X86_64_JUMP_SLO 0000000000000000 puts@GLIBC_2.2.5 + 0
000000200fb0  000300000007 R_X86_64_JUMP_SLO 0000000000000000 strlen@GLIBC_2.2.5 + 0
000000200fb8  000400000007 R_X86_64_JUMP_SLO 0000000000000000 __stack_chk_fail@GLIBC_2.4 + 0
000000200fc0  000500000007 R_X86_64_JUMP_SLO 0000000000000000 printf@GLIBC_2.2.5 + 0
000000200fc8  000800000007 R_X86_64_JUMP_SLO 0000000000000000 __isoc99_scanf@GLIBC_2.7 + 0
000000200fd0  000900000007 R_X86_64_JUMP_SLO 0000000000000000 exit@GLIBC_2.2.5 + 0

The decoding of unwind sections for machine type Advanced Micro Devices X86-64 is not currently supported.

Symbol table '.dynsym' contains 12 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND strlen@GLIBC_2.2.5 (2)
     4: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __stack_chk_fail@GLIBC_2.4 (3)
     5: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@GLIBC_2.2.5 (2)
     6: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.2.5 (2)
     7: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
     8: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __isoc99_scanf@GLIBC_2.7 (4)
     9: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@GLIBC_2.2.5 (2)
    10: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    11: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@GLIBC_2.2.5 (2)

Symbol table '.symtab' contains 69 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000238     0 SECTION LOCAL  DEFAULT    1 
     2: 0000000000000254     0 SECTION LOCAL  DEFAULT    2 
     3: 0000000000000274     0 SECTION LOCAL  DEFAULT    3 
     4: 0000000000000298     0 SECTION LOCAL  DEFAULT    4 
     5: 00000000000002b8     0 SECTION LOCAL  DEFAULT    5 
     6: 00000000000003d8     0 SECTION LOCAL  DEFAULT    6 
     7: 00000000000004a2     0 SECTION LOCAL  DEFAULT    7 
     8: 00000000000004c0     0 SECTION LOCAL  DEFAULT    8 
     9: 0000000000000500     0 SECTION LOCAL  DEFAULT    9 
    10: 00000000000005c0     0 SECTION LOCAL  DEFAULT   10 
    11: 0000000000000650     0 SECTION LOCAL  DEFAULT   11 
    12: 0000000000000670     0 SECTION LOCAL  DEFAULT   12 
    13: 00000000000006e0     0 SECTION LOCAL  DEFAULT   13 
    14: 00000000000006f0     0 SECTION LOCAL  DEFAULT   14 
    15: 00000000000009b4     0 SECTION LOCAL  DEFAULT   15 
    16: 00000000000009c0     0 SECTION LOCAL  DEFAULT   16 
    17: 00000000000009fc     0 SECTION LOCAL  DEFAULT   17 
    18: 0000000000000a40     0 SECTION LOCAL  DEFAULT   18 
    19: 0000000000200d90     0 SECTION LOCAL  DEFAULT   19 
    20: 0000000000200d98     0 SECTION LOCAL  DEFAULT   20 
    21: 0000000000200da0     0 SECTION LOCAL  DEFAULT   21 
    22: 0000000000200f90     0 SECTION LOCAL  DEFAULT   22 
    23: 0000000000201000     0 SECTION LOCAL  DEFAULT   23 
    24: 0000000000201010     0 SECTION LOCAL  DEFAULT   24 
    25: 0000000000000000     0 SECTION LOCAL  DEFAULT   25 
    26: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    27: 0000000000000720     0 FUNC    LOCAL  DEFAULT   14 deregister_tm_clones
    28: 0000000000000760     0 FUNC    LOCAL  DEFAULT   14 register_tm_clones
    29: 00000000000007b0     0 FUNC    LOCAL  DEFAULT   14 __do_global_dtors_aux
    30: 0000000000201010     1 OBJECT  LOCAL  DEFAULT   24 completed.7697
    31: 0000000000200d98     0 OBJECT  LOCAL  DEFAULT   20 __do_global_dtors_aux_fin
    32: 00000000000007f0     0 FUNC    LOCAL  DEFAULT   14 frame_dummy
    33: 0000000000200d90     0 OBJECT  LOCAL  DEFAULT   19 __frame_dummy_init_array_
    34: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS keygen.c
    35: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    36: 0000000000000b6c     0 OBJECT  LOCAL  DEFAULT   18 __FRAME_END__
    37: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS 
    38: 0000000000200d98     0 NOTYPE  LOCAL  DEFAULT   19 __init_array_end
    39: 0000000000200da0     0 OBJECT  LOCAL  DEFAULT   21 _DYNAMIC
    40: 0000000000200d90     0 NOTYPE  LOCAL  DEFAULT   19 __init_array_start
    41: 00000000000009fc     0 NOTYPE  LOCAL  DEFAULT   17 __GNU_EH_FRAME_HDR
    42: 0000000000200f90     0 OBJECT  LOCAL  DEFAULT   22 _GLOBAL_OFFSET_TABLE_
    43: 00000000000009b0     2 FUNC    GLOBAL DEFAULT   14 __libc_csu_fini
    44: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
    45: 0000000000201000     0 NOTYPE  WEAK   DEFAULT   23 data_start
    46: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@@GLIBC_2.2.5
    47: 0000000000201010     0 NOTYPE  GLOBAL DEFAULT   23 _edata
    48: 00000000000009b4     0 FUNC    GLOBAL DEFAULT   15 _fini
    49: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND strlen@@GLIBC_2.2.5
    50: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __stack_chk_fail@@GLIBC_2
    51: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND printf@@GLIBC_2.2.5
    52: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@@GLIBC_
    53: 0000000000201000     0 NOTYPE  GLOBAL DEFAULT   23 __data_start
    54: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    55: 0000000000201008     0 OBJECT  GLOBAL HIDDEN    23 __dso_handle
    56: 00000000000009c0     4 OBJECT  GLOBAL DEFAULT   16 _IO_stdin_used
    57: 0000000000000940   101 FUNC    GLOBAL DEFAULT   14 __libc_csu_init
    58: 0000000000201018     0 NOTYPE  GLOBAL DEFAULT   24 _end
    59: 00000000000006f0    43 FUNC    GLOBAL DEFAULT   14 _start
    60: 0000000000201010     0 NOTYPE  GLOBAL DEFAULT   24 __bss_start
    61: 00000000000008be   119 FUNC    GLOBAL DEFAULT   14 main
    62: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __isoc99_scanf@@GLIBC_2.7
    63: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND exit@@GLIBC_2.2.5
    64: 0000000000201010     0 OBJECT  GLOBAL HIDDEN    23 __TMC_END__
    65: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    66: 00000000000007fa   196 FUNC    GLOBAL DEFAULT   14 check_key
    67: 0000000000000000     0 FUNC    WEAK   DEFAULT  UND __cxa_finalize@@GLIBC_2.2
    68: 0000000000000650     0 FUNC    GLOBAL DEFAULT   11 _init

Version symbols section '.gnu.version' contains 12 entries:
 Addr: 0x00000000000004a2  Offset: 0x0004a2  Link: 5 (.dynsym)
  000:   0 (*local*)       0 (*local*)       2 (GLIBC_2.2.5)   2 (GLIBC_2.2.5)
  004:   3 (GLIBC_2.4)     2 (GLIBC_2.2.5)   2 (GLIBC_2.2.5)   0 (*local*)    
  008:   4 (GLIBC_2.7)     2 (GLIBC_2.2.5)   0 (*local*)       2 (GLIBC_2.2.5)

Version needs section '.gnu.version_r' contains 1 entry:
 Addr: 0x00000000000004c0  Offset: 0x0004c0  Link: 6 (.dynstr)
  000000: Version: 1  File: libc.so.6  Cnt: 3
  0x0010:   Name: GLIBC_2.7  Flags: none  Version: 4
  0x0020:   Name: GLIBC_2.4  Flags: none  Version: 3
  0x0030:   Name: GLIBC_2.2.5  Flags: none  Version: 2

Displaying notes found in: .note.ABI-tag
  Owner                Data size 	Description
  GNU                  0x00000010	NT_GNU_ABI_TAG (ABI version tag)
    OS: Linux, ABI: 3.2.0

Displaying notes found in: .note.gnu.build-id
  Owner                Data size 	Description
  GNU                  0x00000014	NT_GNU_BUILD_ID (unique build ID bitstring)
    Build ID: 2ef368e97b5763a497e168b8a53ca6efb54ab8df
  
$ strings -t d -d ./keygen.bin
    568 /lib64/ld-linux-x86-64.so.2
    985 libc.so.6
    995 exit
   1000 __isoc99_scanf
   1015 puts
   1020 __stack_chk_fail
   1037 printf
   1044 strlen
   1051 __cxa_finalize
   1066 __libc_start_main
   1084 GLIBC_2.7
   1094 GLIBC_2.4
   1104 GLIBC_2.2.5
   1116 _ITM_deregisterTMCloneTable
   1144 __gmon_start__
   1159 _ITM_registerTMCloneTable
   1649 5"	 
   1655 %$	 
   1665 %"	 
   2368 AWAVI
   2375 AUATL
   2458 []A\A]A^A_
   2500 Nope <3
   2508 Give me a pass
   2526 You made it, now keygen me!
   2727 ;*3$"
```

## Assembly extraido via objdump:

```bash
$ objdump -M intel -d -C ./keygen.bin
```

```asm
./keygen.bin:     file format elf64-x86-64

Disassembly of section .init:

0000000000000650 <_init>:
 650:	48 83 ec 08          	sub    rsp,0x8
 654:	48 8b 05 8d 09 20 00 	mov    rax,QWORD PTR [rip+0x20098d]        # 200fe8 <__gmon_start__>
 65b:	48 85 c0             	test   rax,rax
 65e:	74 02                	je     662 <_init+0x12>
 660:	ff d0                	call   rax
 662:	48 83 c4 08          	add    rsp,0x8
 666:	c3                   	ret    

Disassembly of section .plt:

0000000000000670 <.plt>:
 670:	ff 35 22 09 20 00    	push   QWORD PTR [rip+0x200922]        # 200f98 <_GLOBAL_OFFSET_TABLE_+0x8>
 676:	ff 25 24 09 20 00    	jmp    QWORD PTR [rip+0x200924]        # 200fa0 <_GLOBAL_OFFSET_TABLE_+0x10>
 67c:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]

0000000000000680 <puts@plt>:
 680:	ff 25 22 09 20 00    	jmp    QWORD PTR [rip+0x200922]        # 200fa8 <puts@GLIBC_2.2.5>
 686:	68 00 00 00 00       	push   0x0
 68b:	e9 e0 ff ff ff       	jmp    670 <.plt>

0000000000000690 <strlen@plt>:
 690:	ff 25 1a 09 20 00    	jmp    QWORD PTR [rip+0x20091a]        # 200fb0 <strlen@GLIBC_2.2.5>
 696:	68 01 00 00 00       	push   0x1
 69b:	e9 d0 ff ff ff       	jmp    670 <.plt>

00000000000006a0 <__stack_chk_fail@plt>:
 6a0:	ff 25 12 09 20 00    	jmp    QWORD PTR [rip+0x200912]        # 200fb8 <__stack_chk_fail@GLIBC_2.4>
 6a6:	68 02 00 00 00       	push   0x2
 6ab:	e9 c0 ff ff ff       	jmp    670 <.plt>

00000000000006b0 <printf@plt>:
 6b0:	ff 25 0a 09 20 00    	jmp    QWORD PTR [rip+0x20090a]        # 200fc0 <printf@GLIBC_2.2.5>
 6b6:	68 03 00 00 00       	push   0x3
 6bb:	e9 b0 ff ff ff       	jmp    670 <.plt>

00000000000006c0 <__isoc99_scanf@plt>:
 6c0:	ff 25 02 09 20 00    	jmp    QWORD PTR [rip+0x200902]        # 200fc8 <__isoc99_scanf@GLIBC_2.7>
 6c6:	68 04 00 00 00       	push   0x4
 6cb:	e9 a0 ff ff ff       	jmp    670 <.plt>

00000000000006d0 <exit@plt>:
 6d0:	ff 25 fa 08 20 00    	jmp    QWORD PTR [rip+0x2008fa]        # 200fd0 <exit@GLIBC_2.2.5>
 6d6:	68 05 00 00 00       	push   0x5
 6db:	e9 90 ff ff ff       	jmp    670 <.plt>

Disassembly of section .plt.got:

00000000000006e0 <__cxa_finalize@plt>:
 6e0:	ff 25 12 09 20 00    	jmp    QWORD PTR [rip+0x200912]        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 6e6:	66 90                	xchg   ax,ax

Disassembly of section .text:

00000000000006f0 <_start>:
 6f0:	31 ed                	xor    ebp,ebp
 6f2:	49 89 d1             	mov    r9,rdx
 6f5:	5e                   	pop    rsi
 6f6:	48 89 e2             	mov    rdx,rsp
 6f9:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
 6fd:	50                   	push   rax
 6fe:	54                   	push   rsp
 6ff:	4c 8d 05 aa 02 00 00 	lea    r8,[rip+0x2aa]        # 9b0 <__libc_csu_fini>
 706:	48 8d 0d 33 02 00 00 	lea    rcx,[rip+0x233]        # 940 <__libc_csu_init>
 70d:	48 8d 3d aa 01 00 00 	lea    rdi,[rip+0x1aa]        # 8be <main>
 714:	ff 15 c6 08 20 00    	call   QWORD PTR [rip+0x2008c6]        # 200fe0 <__libc_start_main@GLIBC_2.2.5>
 71a:	f4                   	hlt    
 71b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000000720 <deregister_tm_clones>:
 720:	48 8d 3d e9 08 20 00 	lea    rdi,[rip+0x2008e9]        # 201010 <__TMC_END__>
 727:	55                   	push   rbp
 728:	48 8d 05 e1 08 20 00 	lea    rax,[rip+0x2008e1]        # 201010 <__TMC_END__>
 72f:	48 39 f8             	cmp    rax,rdi
 732:	48 89 e5             	mov    rbp,rsp
 735:	74 19                	je     750 <deregister_tm_clones+0x30>
 737:	48 8b 05 9a 08 20 00 	mov    rax,QWORD PTR [rip+0x20089a]        # 200fd8 <_ITM_deregisterTMCloneTable>
 73e:	48 85 c0             	test   rax,rax
 741:	74 0d                	je     750 <deregister_tm_clones+0x30>
 743:	5d                   	pop    rbp
 744:	ff e0                	jmp    rax
 746:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 74d:	00 00 00 
 750:	5d                   	pop    rbp
 751:	c3                   	ret    
 752:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 756:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 75d:	00 00 00 

0000000000000760 <register_tm_clones>:
 760:	48 8d 3d a9 08 20 00 	lea    rdi,[rip+0x2008a9]        # 201010 <__TMC_END__>
 767:	48 8d 35 a2 08 20 00 	lea    rsi,[rip+0x2008a2]        # 201010 <__TMC_END__>
 76e:	55                   	push   rbp
 76f:	48 29 fe             	sub    rsi,rdi
 772:	48 89 e5             	mov    rbp,rsp
 775:	48 c1 fe 03          	sar    rsi,0x3
 779:	48 89 f0             	mov    rax,rsi
 77c:	48 c1 e8 3f          	shr    rax,0x3f
 780:	48 01 c6             	add    rsi,rax
 783:	48 d1 fe             	sar    rsi,1
 786:	74 18                	je     7a0 <register_tm_clones+0x40>
 788:	48 8b 05 61 08 20 00 	mov    rax,QWORD PTR [rip+0x200861]        # 200ff0 <_ITM_registerTMCloneTable>
 78f:	48 85 c0             	test   rax,rax
 792:	74 0c                	je     7a0 <register_tm_clones+0x40>
 794:	5d                   	pop    rbp
 795:	ff e0                	jmp    rax
 797:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
 79e:	00 00 
 7a0:	5d                   	pop    rbp
 7a1:	c3                   	ret    
 7a2:	0f 1f 40 00          	nop    DWORD PTR [rax+0x0]
 7a6:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 7ad:	00 00 00 

00000000000007b0 <__do_global_dtors_aux>:
 7b0:	80 3d 59 08 20 00 00 	cmp    BYTE PTR [rip+0x200859],0x0        # 201010 <__TMC_END__>
 7b7:	75 2f                	jne    7e8 <__do_global_dtors_aux+0x38>
 7b9:	48 83 3d 37 08 20 00 	cmp    QWORD PTR [rip+0x200837],0x0        # 200ff8 <__cxa_finalize@GLIBC_2.2.5>
 7c0:	00 
 7c1:	55                   	push   rbp
 7c2:	48 89 e5             	mov    rbp,rsp
 7c5:	74 0c                	je     7d3 <__do_global_dtors_aux+0x23>
 7c7:	48 8b 3d 3a 08 20 00 	mov    rdi,QWORD PTR [rip+0x20083a]        # 201008 <__dso_handle>
 7ce:	e8 0d ff ff ff       	call   6e0 <__cxa_finalize@plt>
 7d3:	e8 48 ff ff ff       	call   720 <deregister_tm_clones>
 7d8:	c6 05 31 08 20 00 01 	mov    BYTE PTR [rip+0x200831],0x1        # 201010 <__TMC_END__>
 7df:	5d                   	pop    rbp
 7e0:	c3                   	ret    
 7e1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
 7e8:	f3 c3                	repz ret 
 7ea:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]

00000000000007f0 <frame_dummy>:
 7f0:	55                   	push   rbp
 7f1:	48 89 e5             	mov    rbp,rsp
 7f4:	5d                   	pop    rbp
 7f5:	e9 66 ff ff ff       	jmp    760 <register_tm_clones>

00000000000007fa <check_key>:
 7fa:	55                   	push   rbp
 7fb:	48 89 e5             	mov    rbp,rsp
 7fe:	53                   	push   rbx
 7ff:	48 83 ec 28          	sub    rsp,0x28
 803:	48 89 7d d8          	mov    QWORD PTR [rbp-0x28],rdi
 807:	c7 45 e8 00 00 00 00 	mov    DWORD PTR [rbp-0x18],0x0
 80e:	c7 45 ec 00 00 00 00 	mov    DWORD PTR [rbp-0x14],0x0
 815:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
 819:	48 89 c7             	mov    rdi,rax
 81c:	e8 6f fe ff ff       	call   690 <strlen@plt>
 821:	48 83 f8 07          	cmp    rax,0x7
 825:	76 12                	jbe    839 <check_key+0x3f>
 827:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
 82b:	48 89 c7             	mov    rdi,rax
 82e:	e8 5d fe ff ff       	call   690 <strlen@plt>
 833:	48 83 f8 0a          	cmp    rax,0xa
 837:	76 1b                	jbe    854 <check_key+0x5a>
 839:	48 8d 3d 84 01 00 00 	lea    rdi,[rip+0x184]        # 9c4 <_IO_stdin_used+0x4>
 840:	b8 00 00 00 00       	mov    eax,0x0
 845:	e8 66 fe ff ff       	call   6b0 <printf@plt>
 84a:	bf 00 00 00 00       	mov    edi,0x0
 84f:	e8 7c fe ff ff       	call   6d0 <exit@plt>
 854:	c7 45 e8 00 00 00 00 	mov    DWORD PTR [rbp-0x18],0x0
 85b:	eb 1a                	jmp    877 <check_key+0x7d>
 85d:	8b 45 e8             	mov    eax,DWORD PTR [rbp-0x18]
 860:	48 63 d0             	movsxd rdx,eax
 863:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
 867:	48 01 d0             	add    rax,rdx
 86a:	0f b6 00             	movzx  eax,BYTE PTR [rax]
 86d:	0f be c0             	movsx  eax,al
 870:	01 45 ec             	add    DWORD PTR [rbp-0x14],eax
 873:	83 45 e8 01          	add    DWORD PTR [rbp-0x18],0x1
 877:	8b 45 e8             	mov    eax,DWORD PTR [rbp-0x18]
 87a:	48 63 d8             	movsxd rbx,eax
 87d:	48 8b 45 d8          	mov    rax,QWORD PTR [rbp-0x28]
 881:	48 89 c7             	mov    rdi,rax
 884:	e8 07 fe ff ff       	call   690 <strlen@plt>
 889:	48 39 c3             	cmp    rbx,rax
 88c:	72 cf                	jb     85d <check_key+0x63>
 88e:	81 7d ec e7 03 00 00 	cmp    DWORD PTR [rbp-0x14],0x3e7
 895:	7f 1b                	jg     8b2 <check_key+0xb8>
 897:	48 8d 3d 26 01 00 00 	lea    rdi,[rip+0x126]        # 9c4 <_IO_stdin_used+0x4>
 89e:	b8 00 00 00 00       	mov    eax,0x0
 8a3:	e8 08 fe ff ff       	call   6b0 <printf@plt>
 8a8:	bf 00 00 00 00       	mov    edi,0x0
 8ad:	e8 1e fe ff ff       	call   6d0 <exit@plt>
 8b2:	b8 01 00 00 00       	mov    eax,0x1
 8b7:	48 83 c4 28          	add    rsp,0x28
 8bb:	5b                   	pop    rbx
 8bc:	5d                   	pop    rbp
 8bd:	c3                   	ret    

00000000000008be <main>:
 8be:	55                   	push   rbp
 8bf:	48 89 e5             	mov    rbp,rsp
 8c2:	48 83 ec 70          	sub    rsp,0x70
 8c6:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
 8cd:	00 00 
 8cf:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
 8d3:	31 c0                	xor    eax,eax
 8d5:	48 8d 3d f0 00 00 00 	lea    rdi,[rip+0xf0]        # 9cc <_IO_stdin_used+0xc>
 8dc:	e8 9f fd ff ff       	call   680 <puts@plt>
 8e1:	48 8d 45 90          	lea    rax,[rbp-0x70]
 8e5:	48 89 c6             	mov    rsi,rax
 8e8:	48 8d 3d ec 00 00 00 	lea    rdi,[rip+0xec]        # 9db <_IO_stdin_used+0x1b>
 8ef:	b8 00 00 00 00       	mov    eax,0x0
 8f4:	e8 c7 fd ff ff       	call   6c0 <__isoc99_scanf@plt>
 8f9:	48 8d 45 90          	lea    rax,[rbp-0x70]
 8fd:	48 89 c7             	mov    rdi,rax
 900:	e8 f5 fe ff ff       	call   7fa <check_key>
 905:	85 c0                	test   eax,eax
 907:	74 11                	je     91a <main+0x5c>
 909:	48 8d 3d ce 00 00 00 	lea    rdi,[rip+0xce]        # 9de <_IO_stdin_used+0x1e>
 910:	b8 00 00 00 00       	mov    eax,0x0
 915:	e8 96 fd ff ff       	call   6b0 <printf@plt>
 91a:	b8 00 00 00 00       	mov    eax,0x0
 91f:	48 8b 55 f8          	mov    rdx,QWORD PTR [rbp-0x8]
 923:	64 48 33 14 25 28 00 	xor    rdx,QWORD PTR fs:0x28
 92a:	00 00 
 92c:	74 05                	je     933 <main+0x75>
 92e:	e8 6d fd ff ff       	call   6a0 <__stack_chk_fail@plt>
 933:	c9                   	leave  
 934:	c3                   	ret    
 935:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 93c:	00 00 00 
 93f:	90                   	nop

0000000000000940 <__libc_csu_init>:
 940:	41 57                	push   r15
 942:	41 56                	push   r14
 944:	49 89 d7             	mov    r15,rdx
 947:	41 55                	push   r13
 949:	41 54                	push   r12
 94b:	4c 8d 25 3e 04 20 00 	lea    r12,[rip+0x20043e]        # 200d90 <__frame_dummy_init_array_entry>
 952:	55                   	push   rbp
 953:	48 8d 2d 3e 04 20 00 	lea    rbp,[rip+0x20043e]        # 200d98 <__do_global_dtors_aux_fini_array_entry>
 95a:	53                   	push   rbx
 95b:	41 89 fd             	mov    r13d,edi
 95e:	49 89 f6             	mov    r14,rsi
 961:	4c 29 e5             	sub    rbp,r12
 964:	48 83 ec 08          	sub    rsp,0x8
 968:	48 c1 fd 03          	sar    rbp,0x3
 96c:	e8 df fc ff ff       	call   650 <_init>
 971:	48 85 ed             	test   rbp,rbp
 974:	74 20                	je     996 <__libc_csu_init+0x56>
 976:	31 db                	xor    ebx,ebx
 978:	0f 1f 84 00 00 00 00 	nop    DWORD PTR [rax+rax*1+0x0]
 97f:	00 
 980:	4c 89 fa             	mov    rdx,r15
 983:	4c 89 f6             	mov    rsi,r14
 986:	44 89 ef             	mov    edi,r13d
 989:	41 ff 14 dc          	call   QWORD PTR [r12+rbx*8]
 98d:	48 83 c3 01          	add    rbx,0x1
 991:	48 39 dd             	cmp    rbp,rbx
 994:	75 ea                	jne    980 <__libc_csu_init+0x40>
 996:	48 83 c4 08          	add    rsp,0x8
 99a:	5b                   	pop    rbx
 99b:	5d                   	pop    rbp
 99c:	41 5c                	pop    r12
 99e:	41 5d                	pop    r13
 9a0:	41 5e                	pop    r14
 9a2:	41 5f                	pop    r15
 9a4:	c3                   	ret    
 9a5:	90                   	nop
 9a6:	66 2e 0f 1f 84 00 00 	nop    WORD PTR cs:[rax+rax*1+0x0]
 9ad:	00 00 00 

00000000000009b0 <__libc_csu_fini>:
 9b0:	f3 c3                	repz ret 

Disassembly of section .fini:

00000000000009b4 <_fini>:
 9b4:	48 83 ec 08          	sub    rsp,0x8
 9b8:	48 83 c4 08          	add    rsp,0x8
 9bc:	c3                   	ret    
```

## Ponto de entrada do binário

Através do resultado do readelf, podemos ver que a entrada do binário está em: `Entry point address: 0x6f0`

## Análise e RE:
Após algum tempo de análise, encontra-se um método chamado `check_key`, dentro dele é feita a validação de chaves.
Existem duas comparações de tamanho de string, para saber se a chave tem o tamanho esperado, estas estão em:
```asm
 821:	48 83 f8 07          	cmp    rax,0x7 
 825:	76 12                	jbe    839 <check_key+0x3f>
 ...
 833:	48 83 f8 0a          	cmp    rax,0xa
 837:	76 1b                	jbe    854 <check_key+0x5a>
```

Ou seja, caso a string fornecida tiver menos do que 10 caracteres (primeiro menor-igual a 7, depois, menor-igual a 10 (0xa)), é desviado para o fim do programa.
Sendo assim, a chave tem ao menos 10 caracteres.

Após mais algumas tentativas de chaves e debugging (veja arquivo [disas.txt](disas.txt)), é encontrada a ultima comparação que pode desviar para o fim do arquivo, nela tem o magic number 0x3e7.
Convertendo para decimal, resulta em 999, ou seja, a somatória dos caracteres (de acordo com a tabela ascii), deve resultar em 999.

```asm
 88e:	81 7d ec e7 03 00 00 	cmp    DWORD PTR [rbp-0x14],0x3e7
 895:	7f 1b                	jg     8b2 <check_key+0xb8>
```

Durante o debug foi identificado que $rbp-0x14 contém a somatória dos caracteres ascii, isto é feito dentro de um for que usa como range a quantidade de caracteres fornecidos.
Logo, se tentarmos a seguinte chave ddddddddde, teremos uma resposta válida (d=0x64(100), e=0x65(101), então, d*10+e = 900+101=1001) 

```bash
$ ./keygen.bin                           
Give me a pass
ddddddddde
You made it, now keygen me!%     
```
