#!/bin/bash

# DeepSeek API Key Setup Script
# This script helps you set up your DeepSeek API key for the Agno demo

echo "================================================"
echo "DeepSeek API Key Setup for Agno Demo"
echo "================================================"
echo ""

# Check if API key is already set
if [ -n "$DEEPSEEK_API_KEY" ]; then
    echo "✓ DEEPSEEK_API_KEY is already set in your environment"
    echo "  Current value: ${DEEPSEEK_API_KEY:0:10}..."
    echo ""
    read -p "Do you want to update it? (y/n): " update_key
    if [ "$update_key" != "y" ]; then
        echo "Keeping existing API key."
        exit 0
    fi
fi

# Prompt for API key
echo "Please enter your DeepSeek API key:"
echo "(Get one at: https://platform.deepseek.com/)"
echo ""
read -p "API Key: " api_key

if [ -z "$api_key" ]; then
    echo "❌ Error: No API key provided"
    exit 1
fi

# Export for current session
export DEEPSEEK_API_KEY="$api_key"
echo ""
echo "✓ API key set for current session"

# Ask if user wants to persist
echo ""
read -p "Do you want to save this to your shell configuration? (y/n): " save_config

if [ "$save_config" = "y" ]; then
    # Detect shell
    if [ -n "$ZSH_VERSION" ]; then
        shell_config="$HOME/.zshrc"
    elif [ -n "$BASH_VERSION" ]; then
        shell_config="$HOME/.bashrc"
    else
        shell_config="$HOME/.profile"
    fi
    
    # Check if already exists in config
    if grep -q "DEEPSEEK_API_KEY" "$shell_config" 2>/dev/null; then
        echo "⚠️  DEEPSEEK_API_KEY already exists in $shell_config"
        read -p "Do you want to update it? (y/n): " update_config
        if [ "$update_config" = "y" ]; then
            # Remove old entry and add new one
            sed -i.bak '/DEEPSEEK_API_KEY/d' "$shell_config"
            echo "export DEEPSEEK_API_KEY=\"$api_key\"" >> "$shell_config"
            echo "✓ Updated API key in $shell_config"
        fi
    else
        # Add to config
        echo "" >> "$shell_config"
        echo "# DeepSeek API Key for Agno" >> "$shell_config"
        echo "export DEEPSEEK_API_KEY=\"$api_key\"" >> "$shell_config"
        echo "✓ Added API key to $shell_config"
    fi
    
    echo ""
    echo "Note: Restart your terminal or run:"
    echo "  source $shell_config"
fi

echo ""
echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "You can now run the demo with:"
echo "  python cookbook/demo/run.py"
echo ""
echo "Or activate your virtual environment first:"
echo "  source .demoenv/bin/activate"
echo "  python cookbook/demo/run.py"
echo ""

