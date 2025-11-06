@echo off
REM Build script for HandLingo Frontend (Windows)
REM This script prepares the frontend for deployment

echo 🚀 Building HandLingo Frontend...

REM Navigate to frontend directory
cd frontend

REM Create a simple build verification
echo 📁 Frontend files:
dir

REM Verify all essential files exist
echo 🔍 Verifying essential files...
set "files=index.html login.js lessons.js quiz.js results.js styles.css"
set "missing=0"

for %%f in (%files%) do (
    if exist "%%f" (
        echo ✅ %%f found
    ) else (
        echo ❌ %%f missing
        set "missing=1"
    )
)

if %missing%==1 (
    echo ❌ Build failed - missing files
    exit /b 1
)

echo ✨ Build completed successfully!
echo 📦 Frontend ready for deployment