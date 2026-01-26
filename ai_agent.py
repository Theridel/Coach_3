from pathlib import Path
import os
import sys

# ==============================================================================
# AI AGENT - MODULO DI RILEVAZIONE AMBIENTE
# Versione: 0.1.0 (Basata su logica notebook 0.3.2)
# ==============================================================================

def check_environment():
    # 1.1 Logica di rilevazione migliorata per script .py
    if os.getenv("GITHUB_ACTIONS"):
        ENV = "GITHUB_ACTION"
        ROOT = Path.cwd()
        # GitHub ci dice già su quale branch siamo
        BRANCH = os.getenv("GITHUB_REF_NAME", "unknown")
    elif Path("/content").exists():
        ENV = "COLAB"
        ROOT = Path("/content")
        BRANCH = "sviluppo"
    elif Path("/home/studio-lab-user").exists():
        ENV = "SAGEMAKER"
        ROOT = Path("/home/studio-lab-user")
        BRANCH = "sviluppo"
    else:
        ENV = "LOCAL/UNKNOWN"
        ROOT = Path.cwd()
        BRANCH = "main"

    # 1.2 Configurazione percorsi standard
    # In GitHub Actions, il repo viene clonato direttamente nella cartella corrente
    REPO_LOCAL = ROOT 
    TARGET_MODULES = ROOT / "modules"

    # 1.3 Output di riepilogo
    print(f"{'='*40}")
    print(f"🤖 AI AGENT STATUS")
    print(f"🐍 Python Version: {sys.version.split()[0]}")
    print(f"🌍 AMBIENTE : {ENV}")
    print(f"🌿 BRANCH   : {BRANCH}")
    print(f"📁 ROOT     : {ROOT}")
    print(f"📂 MODULES  : {TARGET_MODULES}")
    print(f"{'='*40}")
    
    return ENV, ROOT, BRANCH

if __name__ == "__main__":
    check_environment()
