#!/bin/bash
# Start Kafka (KRaft mode) and Kafka UI
set -e

echo "🚀 Starting Kafka (KRaft mode - no ZooKeeper)..."
docker compose up -d

echo ""
echo "⏳ Waiting for Kafka to be healthy..."
timeout=60
elapsed=0
while ! docker compose exec -T kafka /opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server localhost:9092 > /dev/null 2>&1; do
    sleep 2
    elapsed=$((elapsed + 2))
    if [ $elapsed -ge $timeout ]; then
        echo "❌ Kafka failed to start within ${timeout}s"
        docker compose logs kafka
        exit 1
    fi
    echo "   ...waiting ($elapsed/${timeout}s)"
done

echo ""
echo "✅ Kafka is running!"
echo ""
echo "📊 Kafka UI:  http://localhost:8080"
echo "🔌 Bootstrap: localhost:9092"
echo ""
echo "💡 Run your first producer:  python lessons/01_producer.py"
