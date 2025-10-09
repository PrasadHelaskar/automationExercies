#!/bin/bash

source shellFiles/env_selector.sh

select_env "$1"

echo "Selected Env: $TEST_ENV_FILE"

set -a 
source "$TEST_ENV_FILE"
set +a

echo "This is Pytest Runner File"
echo "Select Number to trigger the Execution"
echo "1. For the Selenium Scripts"
echo "2. For the API Scripts"
echo "3. For Parallel Selenium Execution"
echo "4. For Parallel API Execution"
echo ""

read command

if [ "$command" = "1" ]; then
    
    echo "Selenium Scripts"
    echo "Enter the log level:"
    read log_level
    echo "Enter the test file:"
    read path

    pytest -v --log-cli-level="${log_level:-info}" "seleniumScripts/testScripts/${path}"

elif [ "$command" = "2" ]; then

    echo "API Scripts"
    echo "Enter the log level:"
    read log_level
    echo "Enter the test file:"
    read path

    pytest -v --log-cli-level="${log_level:-info}" "apiScripts/testScripts/${path}"

elif [ "$command" = "3" ]; then

    echo "Selenium Parallel Scripts (All)"
    echo "Enter the thread count:"
    read thread_count

    pytest -v -n "${thread_count:-3}" "seleniumScripts/testScripts"

elif [ "$command" = "4" ]; then

    echo "API Parallel Scripts (All)"
    echo "Enter the thread count:"
    read thread_count

    pytest -v -n "${thread_count:-3}" "apiScripts/testScripts"

else
    echo "Invalid command"

fi