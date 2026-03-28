# SDS-Prompt-Guard

Este repo usa el dataset de Hugging Face: `MAlmasabiIndirect-Prompt-Injection-BIPIA-GPT`.

## Requisitos

- Python 3.10+

## Crear entorno e instalar dependencias

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Linux/macOS (bash/zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Descargar el dataset a local

Ejecuta el script que descarga y guarda el dataset en disco:

### Windows (PowerShell)

```powershell
python .\data\get_data.py
```

### Linux/macOS (bash/zsh)

```bash
python data/get_data.py
```
