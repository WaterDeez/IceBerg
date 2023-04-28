#!/bin/bash
output=$(curl -s -H "Accept: application/json" -H "Authorization: Bearer $1" $2)
echo $output;