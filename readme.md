# AI FinOps & Governance Router 🚀

## BLUF (Bottom Line Up Front)
Middleware de inferencia agnóstico diseñado para reducir costes de LLM en entornos empresariales mediante caching semántico y enrutamiento inteligente. 

**Hipótesis de diseño (no medida):** Reducción ≥ 30% en el consumo mensual de tokens en arquitecturas de producción.

## Arquitectura propuesta (no implementada)

Cliente → autenticación y políticas → presupuesto por tenant → control de PII → caché autorizada → adaptador LLM → métricas y auditoría.

La caché debe aislar tenants y evitar reutilizar datos sensibles sin autorización. El sistema debe abstenerse ante clasificación incierta.

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

## Demo de caché exacta

Ejecuta `python demo_cache.py` con Python 3, sin dependencias. La prueba compara cinco solicitudes sintéticas con y sin caché exacta. Una solicitud idéntica de otro equipo provoca una llamada independiente. La métrica muestra llamadas evitadas y tokens simulados. El ahorro real y la caché semántica siguen pendientes de validación.

## Roadmap & Scalability
Arquitectura desacoplada propuesta. Kubernetes y alta disponibilidad quedan fuera del MVP. Primero validar coste por solicitud, tasa de aciertos de caché, calidad de respuestas y aislamiento entre tenants.

> **Estado:** concepto de producto; incluye una demostración local de caché exacta. El middleware de producción y su benchmark quedan pendientes.