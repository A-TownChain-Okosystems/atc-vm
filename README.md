# atc-vm

ShivaVM — Smart Contract Virtual Machine für A-TownChain.

Wird aus atc-shivacore/kernel/src/vm.rs (K-Sprint 19) als eigenständiges Repo
ausgelagert, sobald der VM-Code zu groß für das Kernel-Repo wird.

## Features (bestehend aus K19)
- 27 Opcodes (Arithmetic, Stack, Memory, Storage, Control Flow)
- Stack-Interpreter (1024 Slots)
- Gas-Metering (Per-Instruction Cost)
- Contract-Storage (Key-Value)
- Call/Return (rekursive Contracts)
- Event-Logging

## Geplante Erweiterungen
- JIT-Compilation (Hot-Path Optimierung)
- Bytecode-Verification
- Formal-Verification-Interface
- Cross-Contract-Calls (async)
- WASM-Fallback (alternative Bytecode)

## Build
```bash
cargo build --target x86_64-unknown-none
```

## Abhängigkeiten
- [atc-shivacore](https://github.com/A-TownChain-Okosystems/atc-shivacore) — Kernel-Integration

## Status
- Initial: Repo erstellt 05.08.2026
- Sprache: Rust (no_std)
- Ursprung: K-Sprint 19 (vm.rs im Kernel)

---
Copyright © Michael Wroblewski / A-TownChain-Okosystems. All Rights Reserved.
