@echo off
echo PREPARING TO INSTALL REPOSITORY...

REM Python sürüm kontrolü
python --version 2>nul
IF %ERRORLEVEL% NEQ 0 (
    REM Python yüklü değilse
    echo YOU NEED TO INSTALL PYTHON
    pause
    exit
)

REM Python sürüm kontrolü
python -c "import sys; exit(1) if sys.version_info.major < 3 else exit(0)"
IF %ERRORLEVEL% NEQ 0 (
    REM Python 3 ve üzeri değilse
    echo YOU NEED TO INSTALL PYTHON 3 OR HIGHER
    pause
    exit
)

REM pip kurulu olup olmadığını kontrol et
pip --version 2>nul
IF %ERRORLEVEL% NEQ 0 (
    REM pip kurulu değilse
    echo PIP INSTALLING...
    python get-pip.py
    IF %ERRORLEVEL% NEQ 0 (
        REM pip yüklenemediyse
        echo PIP INSTALLATION ERROR
        pause
        exit
    )
)

REM Kütüphaneleri yükle
FOR /F %%i IN (requirements.txt) DO (
    pip show %%i >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        REM Kütüphane yüklü değilse
        echo %%i INSTALLING...
        pip install %%i
        IF %ERRORLEVEL% NEQ 0 (
            REM Kütüphane yüklenemediyse
            echo %%i INSTALLATION ERROR
            pause
            exit
        )
    )
)

REM Kurulum tamamlandı
echo -----INSTALLATION COMPLETED-------
echo - YOU CAN USE THE REPOSITORY NOW -
pause
exit
