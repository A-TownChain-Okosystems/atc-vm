# ATC-VM — ATCLang Virtual Machine

Die ATCLang Virtual Machine führt ATCLang-Bytecode aus. Teil des A-TownChain OS Ökosystems.

## Architektur
```
┌─────────────────────────────────────────┐
│              ATC-VM                      │
├─────────────────────────────────────────┤
│  ┌─────────┐  ┌──────────┐  ┌─────────┐ │
│  │ Decoder  │→│ Executor │→│ Memory  │ │
│  └─────────┘  └──────────┘  └─────────┘ │
│  ┌─────────┐  ┌──────────┐  ┌─────────┐ │
│  │ Stack   │  │  Heap    │  │  GC     │ │
│  └─────────┘  └──────────┘  └─────────┘ │
│  ┌─────────┐  ┌──────────┐               │
│  │ Gas     │  │ Syscalls │               │
│  └─────────┘  └──────────┘               │
└─────────────────────────────────────────┘
```

## Komponenten
- **Bytecode Decoder** — ATCLang Opcodes → interne Instruktionen
- **Executor** — Stack-basierte Ausführung mit Gas-Metering
- **Memory Manager** — Stack, Heap, Garbage Collection
- **Syscall Interface** — Kernel-Syscalls (ATC-22 bis ATC-30)
- **Gas Meter** — Execution-Kosten-Limit (Anti-DoS)

## Opcode-Kategorien
| Bereich | Opcodes | Beschreibung |
|---------|---------|--------------|
| Stack | PUSH, POP, DUP, SWAP | Stack-Operationen |
| Arithmetic | ADD, SUB, MUL, DIV, MOD | Mathematik |
| Logic | AND, OR, NOT, XOR, CMP | Logik |
| Memory | MLOAD, MSTORE, ALLOC, FREE | Speicher |
| Control | JUMP, JMPIF, CALL, RET | Kontrollfluss |
| Blockchain | HASH, SIGN, VERIFY, BALANCE | Kette |
| Syscall | SYSCALL (ATC-22 bis ATC-30) | Kernel |

## Verwandte Repos
- [atclang](https://github.com/A-TownChain-Okosystems/atclang) — Compiler
- [atc-stdlib](https://github.com/A-TownChain-Okosystems/atc-stdlib) — Standard Library
- [atc-shivacore](https://github.com/A-TownChain-Okosystems/atc-shivacore) — Kernel (Rust)

[agent: aurora-base44-superagent-6a2756186106d6f0fbb105b5]
