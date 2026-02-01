import os
import sys
import subprocess
import threading
from pathlib import Path
import gradio as gr


# ==========================================================
# 1) Rilevamento ambiente (SEMPLICE)
# ==========================================================
def detect_env():
    if os.getenv("RUN_CONTEXT") == "HF_SPACE":
        return "HF_SPACE"
    elif os.getenv("GITHUB_ACTIONS"):
        return "GITHUB_ACTION"
    else:
        return "LOCAL"


ENV = detect_env()


# ==========================================================
# 2) pip check NON bloccante (solo in HF)
#    - Spaces usa variables come env-var a runtime
#      secondo documentazione ufficiale. [1](https://vercel.com/docs/plans/hobby)
#    - Le dipendenze sono installate in fase BUILD
#      tramite requirements.txt del repo dello Space. [2](https://cloudvisor.co/is-amazon-sagemaker-free/)
# ==========================================================
def pip_check_non_blocking(timeout_sec=6):
    def run():
        try:
            print("=== pip check (HF runtime) ===")
            subprocess.run(["pip", "check"], check=False)
            print("=== pip check done ===")
        except Exception as e:
            print(f"[pip_check skipped] {e}")

    t = threading.Thread(target=run, daemon=True)
    t.start()
    t.join(timeout=timeout_sec)


if ENV == "HF_SPACE":
    pip_check_non_blocking()


# ==========================================================
# 3) UI Gradio minima (ZERO CREDITI)
#    - Gli Spaces eseguono Gradio dentro un iframe come
#      parte del runtime ufficiale. [3](https://www.freetiers.com/directory/vercel)
# ==========================================================
def show_env():
    info = [
        f"ENV: {ENV}",
        f"ROOT: {Path.cwd()}",
        f"BRANCH: main" if ENV == "HF_SPACE" else "(n/a)"
    ]
    return "\n".join(info)


# In HF serve una UI da lanciare:
if ENV == "HF_SPACE":
    demo = gr.Interface(
        fn=show_env,
        inputs=None,
        outputs=gr.Textbox(lines=12),
        title="Environment Check (HF)"
    )
    demo.launch()


# ==========================================================
# 4) CLI mode (GitHub Actions / Local)
# ==========================================================
if ENV == "GITHUB_ACTION":
    print("Running inside GitHub Actions.")
    print(show_env())

if ENV == "LOCAL":
    print("Running locally.")
    print(show_env())
