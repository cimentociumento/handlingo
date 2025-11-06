#!/bin/bash
# Build script for HandLingo Frontend
# This script prepares the frontend for deployment

echo "🚀 Building HandLingo Frontend..."

# Navigate to frontend directory
cd frontend

# Create a simple build verification
echo "📁 Frontend files:"
ls -la

# Verify all essential files exist
echo "🔍 Verifying essential files..."
for file in index.html login.js lessons.js quiz.js results.js styles.css; do
    if [ -f "$file" ]; then
        echo "✅ $file found"
    else
        echo "❌ $file missing"
        exit 1
    fi
done

echo "✨ Build completed successfully!"
echo "📦 Frontend ready for deployment"