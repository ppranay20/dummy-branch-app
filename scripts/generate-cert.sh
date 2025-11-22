#!/bin/bash

# Generate self-signed SSL certificate for branchloans.com

echo "Generating self-signed SSL certificate for branchloans.com..."
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout certs/branchloans.com.key \
    -out certs/branchloans.com.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=branchloans.com"
echo "Certificate generated successfully!"
echo "Certificate: certs/branchloans.com.crt"
echo "Private Key: certs/branchloans.com.key"