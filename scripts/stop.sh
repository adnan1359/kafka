#!/bin/bash
# Stop Kafka and free up resources
set -e

echo "🛑 Stopping Kafka..."
docker compose down

echo "✅ Kafka stopped. Resources freed!"
echo ""
echo "💡 To also remove all Kafka data: docker compose down -v"
