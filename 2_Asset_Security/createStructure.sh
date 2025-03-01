# Install virtualenv if you don’t have it already
pip3 install virtualenv

# Create a new environment
virtualenv autoclify_env

# Activate the environment
source autoclify_env/bin/activate  # On MacOS

# Install required libraries
pip3 install flask scikit-learn tensorflow numpy werkzeug joblib