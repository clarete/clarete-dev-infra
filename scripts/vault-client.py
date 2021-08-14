#!/bin/bash

VAULT_ID=""

while [[ $# -gt 0 ]]
do
    key="$1"

    case $key in
        --vault-id)
            VAULT_ID="$2"
            shift;shift;
            ;;
        *)
            usage
            ;;
    esac
done

if [ "$VAULT_ID" != "" ]; then
    exec pass "ansible/$VAULT_ID"
fi
