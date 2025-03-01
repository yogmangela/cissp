#!/bin/bash

# Set the directory paths
FRONTEND_DIR="./frontend"
BACKEND_DIR="./backend"

# Function to ensure package-lock.json exists in frontend
ensure_package_lock() {
    echo "Checking for package-lock.json in the frontend directory..."

    # Check if package-lock.json exists in the frontend directory
    if [ ! -f "$FRONTEND_DIR/package-lock.json" ]; then
        echo "package-lock.json not found. Installing dependencies..."
        # Navigate to the frontend directory and install dependencies
        cd "$FRONTEND_DIR" || exit
        npm install
        cd - || exit
    else
        echo "package-lock.json already exists. Skipping npm install."
    fi
}

# Function to clean old Docker images and containers
clean_docker_cache() {
    echo "Cleaning Docker cache..."
    docker builder prune -f
    docker-compose down
}

# Function to build and start containers
build_and_run_containers() {
    echo "Building and starting containers with Docker Compose..."
    docker-compose up --build
}

# Main process
ensure_package_lock
clean_docker_cache
build_and_run_containers