import PyInstaller.__main__
import os

if __name__ == '__main__':
    print("Building Quantum Dashboard Executable (Standby, this takes a few minutes)...")
    PyInstaller.__main__.run([
        'launcher.py',
        '--name=QuantumDashboard',
        '--onefile',
        '--copy-metadata=streamlit',
        '--hidden-import=streamlit',
        '--hidden-import=qiskit',
        '--hidden-import=qiskit_ibm_runtime',
        '--hidden-import=qiskit_aer',
        '--hidden-import=plotly',
        '--hidden-import=pandas',
        '--hidden-import=numpy',
        '--hidden-import=requests',
        '--hidden-import=yfinance',
        '--hidden-import=scipy',
        '--clean'
    ])
    print("Build Complete! Find your executable in the 'dist' folder.")
