"""Measure exact-match cache reuse with a simulated inference provider."""
from collections import Counter


def run(requests, use_cache):
    cache = {}
    metrics = Counter()
    responses = []

    for tenant, prompt in requests:
        key = (tenant, prompt)
        if use_cache and key in cache:
            metrics["cache_hits"] += 1
        else:
            # Synthetic usage for a mock call, with no tokenizer or provider.
            cache[key] = f"Respuesta de ejemplo: {prompt}"
            metrics["provider_calls"] += 1
            metrics["simulated_tokens"] += 100
        responses.append(cache[key])

    return responses, metrics


def main():
    requests = [
        ("equipo-a", "Resume el informe"),
        ("equipo-a", "Resume el informe"),
        ("equipo-b", "Resume el informe"),
        ("equipo-a", "Explica el presupuesto"),
        ("equipo-a", "Resume el informe"),
    ]
    baseline_responses, baseline = run(requests, use_cache=False)
    cached_responses, cached = run(requests, use_cache=True)
    if baseline_responses != cached_responses or cached["provider_calls"] != 3:
        raise RuntimeError("Las respuestas o el aislamiento de la caché han cambiado")

    saved = baseline["simulated_tokens"] - cached["simulated_tokens"]
    print(f"Llamadas al proveedor simulado: {baseline['provider_calls']} → {cached['provider_calls']}")
    print(f"Aciertos de caché: {cached['cache_hits']}")
    print(f"Tokens simulados evitados: {saved} ({saved / baseline['simulated_tokens']:.0%})")


if __name__ == "__main__":
    main()
