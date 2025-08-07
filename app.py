#!/usr/bin/env python3
"""
Agentic AI Project Entry Point
This is the primary entry point for the Agentic AI application.
It calls the main.py file to start the backend and frontend services.
"""

import sys
import os

# Add the current directory to Python path to ensure imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    try:
        # Import and run the main application
        from app.main import run_backend, run_frontend
        import threading
        import time
        
        print("Starting Agentic AI Application...")
        print("Backend service will start on http://127.0.0.1:9999")
        print("Frontend service will start on http://127.0.0.1:8501")
        print("=" * 50)
        
        # Start backend in a separate thread
        backend_thread = threading.Thread(target=run_backend)
        backend_thread.daemon = True
        backend_thread.start()
        
        # Wait a moment for backend to initialize
        time.sleep(2)
        
        # Start frontend (this will block)
        run_frontend()
        
    except KeyboardInterrupt:
        print("\nAgentic AI Application stopped by user")
    except Exception as e:
        print(f"Error starting Agentic AI Application: {e}")
        sys.exit(1) 