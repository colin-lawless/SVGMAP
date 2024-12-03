# **SVGMAP**

Generate SVG maps with customizable grid overlays for continents, countries, and states using Python.

---

Quick setup commands below - **CHECK GDAL FIRST**

---

Watch the video demonstration here: 



[![Watch the video](https://img.youtube.com/vi/M7HVZWJV9Fg/0.jpg)](https://www.youtube.com/watch?v=M7HVZWJV9Fg)

## **Prerequisites**

### **Ensure GDAL is Installed**

#### **macOS**
1. Install GDAL using Homebrew:
   ```bash
   brew install gdal
   ```
2. Verify installation:
   ```bash
   gdal-config --version
   ```

#### **Windows**
1. Install GDAL:
   - Download the OSGeo4W installer from [https://trac.osgeo.org/osgeo4w/](https://trac.osgeo.org/osgeo4w/).
   - Select "Advanced Install" and install the latest version of GDAL.
2. Add GDAL to PATH:
   - Add `C:\OSGeo4W\bin` to your system PATH:
     - Open **System Properties** → **Advanced** → **Environment Variables**.
     - Edit the `Path` variable to include `C:\OSGeo4W\bin`.
3. Verify installation:
   ```cmd
   gdalinfo --version
   ```

---

## **Setup Instructions**

### **macOS**
1. Clone the repository:
   ```bash
   git clone https://github.com/colin-lawless/SVGMAP.git
   cd SVGMAP
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate
   ```
3. Navigate to the `src` folder:
   ```bash
   cd src
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the script:
   ```bash
   python svgmap.py
   ```

---

### **Windows**
1. Clone the repository:
   ```cmd
   git clone https://github.com/colin-lawless/SVGMAP.git
   cd SVGMAP
   ```
2. Create and activate a virtual environment:
   ```cmd
   python -m venv env
   env\Scripts\activate
   ```
3. Navigate to the `src` folder:
   ```cmd
   cd src
   ```
4. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
5. Run the script:
   ```cmd
   python svgmap.py
   ```

---

## **Usage**

1. **Enter a Region**:
   Enter the name of a continent, country, or state when prompted (e.g., `mexico`).

2. **Choose a Dot Color**:
   Enter a color name (e.g., `red`) or a hex color code (e.g., `#FF5733`).

3. **Set Grid Density**:
   Provide a grid density between 1 (sparse) and 100 (dense).

4. **Output**:
   The generated SVG file will be saved in the `src` folder with the name `{region}-map.svg`.

---

## **COPY AND PASTE THESE COMMANDS - CHECK GDAL FIRST**

### **macOS**
```bash
brew install gdal
git clone https://github.com/colin-lawless/SVGMAP.git
cd SVGMAP
python -m venv env
source env/bin/activate
cd src
pip install -r requirements.txt
python svgmap.py
```

### **Windows**
Download and install GDAL from https://trac.osgeo.org/osgeo4w/.
```cmd
git clone https://github.com/colin-lawless/SVGMAP.git
cd SVGMAP
python -m venv env
env\Scripts\activate
cd src
pip install -r requirements.txt
python svgmap.py
```

---
This project uses Natural Earth's 1:110m Cultural Vectors. You can check it out [here](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).

---
## **License**
MIT License
