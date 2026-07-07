# Architecture Design

## Key Components
- **Orchestrator**: Work distribution and coordination
- **Agent Pool**: 5-100 autonomous security agents
- **KV Store**: Attack state persistence (Redis/ChronosDB)
- **ML Model**: Attack pattern generation (Transformer-based)
- **SIEM Bridge**: Security event monitoring (Elastic Common Schema)

## Communication Protocols
- gRPC with mTLS for inter-service communication
- AMQP for event notifications
- REST for UI integrations

## Performance Goals
- 100k attack patterns stored/day
- 5ms latency between coordinator and any agent
- 100 parallel simulation environments

## Deployment Strategy
Canary deployment pattern with 10% traffic routing to new versions until baseline success rate is validated (99.9% uptime, 50ms SLA)