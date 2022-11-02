#!/bin/sh

# Determine external ip address
if [ -z "$EXTERNAL_IP" ]; then
    EXTERNAL_IP=$(curl -s icanhazip.com)
fi

# Get internal ip address from eth0
if [ -z "$INTERNAL_IP" ]; then
    INTERNAL_IP=$(ip addr show eth0 | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
fi

turnserver --log-file=stdout --external-ip="$EXTERNAL_IP" --listening-ip="$INTERNAL_IP" 
