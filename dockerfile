FROM python:3.11-slim

# Instalace všech knihoven potřebných pro PySide6 a Qt GUI
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libxkbcommon-x11-0 \
    libegl1 \
    libgl1 \
    libfontconfig1 \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    libdbus-1-3 \
    libxcb-xinerama0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-shm0 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxcb-cursor0 \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Zkopíruj celý projekt
COPY . /app

# Instalace Python knihoven
RUN pip install --no-cache-dir PySide6

# Nastavení X serveru
ENV DISPLAY=:0

# Spuštění aplikace
CMD ["python", "bmi.py"]
