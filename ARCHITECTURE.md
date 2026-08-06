# 🌳 Architektur — atc-vm

> **Stand:** 2026-08-06 | **Version:** v1.0.0
> **Teil von:** [A-TownChain Ökosystem](https://github.com/A-TownChain-Okosystems)

## Beschreibung

ATCLang Virtual Machine. Bytecode-Interpreter, Stack, Gas, Opcodes.

## Metadaten

| Metrik | Wert |
|--------|------|
| Layer | L1 — ATCLang |
| Sprint | 2.1 |
| ATC-Standards | ATC-93 |
| Status | 🟠 Aufbau |
| Code-Repo | [atc-vm](https://github.com/A-TownChain-Okosystems/atc-vm) |
| Wiki-Repo | [atc-vm-wiki](https://github.com/A-TownChain-Okosystems/atc-vm-wiki) |

## Komponenten-Übersicht

| Komponente | Beschreibung | Status |
|-----------|-------------|--------|
| `atcvm.py` | VM Core: fetch, decode, execute cycle, stack, memory | 📋 GEPLANT |
| `opcodes.atc` | Opcode-Definitionen: arithmetic, logic, control, crypto, syscall | 📋 GEPLANT |
| `stack.atc` | Stack-Management: push, pop, dup, swap, frame management | 📋 GEPLANT |
| `gas_meter.atc` | Gas-Meter: per-instruction cost, refund, limit enforcement | 📋 GEPLANT |
| `interpreter.atc` | Bytecode-Interpreter: dispatch loop, error handling | 📋 GEPLANT |
| `bytecode_format.atc` | Bytecode-Format: encoding, sections, metadata, checksum | 📋 GEPLANT |

## Architektur-Baum

```
atc-vm/
├── README.md
├── LICENSE
├── .gitignore
├── STATUS.md
├── ROADMAP.md
├── CHANGELOG.md
├── ARCHITECTURE.md
├── FILE_REGISTER.md
├── atcvm.py
├── opcodes.atc
├── stack.atc
├── gas_meter.atc
├── interpreter.atc
├── bytecode_format.atc
```

## Abhängigkeiten

- **ATCLang Stdlib** (atc-stdlib)
- **ATC VM** (atc-vm)
- **ATC Kernel** (atc-kernel)

## Roadmap

| Phase | Aufgabe | Status |
|-------|---------|--------|
| Sprint 2.1 | Komponenten-Definition | ✅ ERLEDIGT |
| Sprint 2.1 | Architektur-Baum | ✅ ERLEDIGT |
| Sprint 2.1 | Stub-Dateien erstellen | 🔄 IN ARBEIT |
| Sprint 2.1 | Implementierung | 📋 GEPLANT |
| Sprint 2.1.1 | Tests | 📋 GEPLANT |
| Sprint 2.1.2 | Dokumentation | 📋 GEPLANT |

---
*Auto-generiert 2026-08-06 · Aurora (MasterBrain · Base44)*
