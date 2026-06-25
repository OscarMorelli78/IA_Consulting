# AI FinOps & Governance Router 🚀

## BLUF (Bottom Line Up Front)
Middleware de inferencia agnóstico diseñado para reducir costes de LLM en entornos empresariales mediante caching semántico y enrutamiento inteligente. 

**Logro esperado:** Reducción ≥ 30% en el consumo mensual de tokens en arquitecturas de producción.

## Arquitectura de Sistema


## Problemática Resuelta
Las empresas actuales sufren de:
- **Costes incontrolados:** Consumo masivo de APIs de IA sin atribución por equipo/proyecto.
- **Vulnerabilidad:** Fugas de PII (Datos de Identificación Personal) en prompts enviados a modelos externos.
- **Ineficiencia:** Redundancia en peticiones de inferencia.

## Core Pillars
1. **Financial Governance:** Monitorización en tiempo real y *Circuit Breaker* financiero por tenant.
2. **Security-First:** Sanitización de datos sensibles antes de la egress hacia proveedores LLM.
3. **Performance Optimization:** Layer de cacheo semántico (Redis + HNSW) para eliminar inferencias redundantes.

## Stack Tecnológico
- **Core:** FastAPI, LiteLLM (Abstraction Layer)
- **Data & Cache:** PostgreSQL (pgvector), Redis
- **Observability:** OpenTelemetry (Tracing & Metrics)

## Roadmap & Scalability
*Desarrollado con arquitectura desacoplada para despliegue en K8s con alta disponibilidad.*

> **Nota:** La lógica del motor de ruteo y optimización se encuentra en módulos privados por motivos de propiedad intelectual. Documentación técnica detallada disponible en `docs/ARCHITECTURE.md`.