# AutoVisionLab

Scaffold for a computer-vision experimentation lab — project structure for training, evaluating, and deploying image-classification models (ResNet-50 / EfficientNet), with config-driven experiments and a FastAPI serving stub.

> **Status: early scaffold.** Directory structure and interfaces are in place; training runs, experiment results, and the serving API are not yet implemented. Not production code.

## Layout

```
configs/       dataset / model / training YAML configs
models/        ResNet-50, EfficientNet definitions
experiments/   experiment runner
evaluation/    metrics + evaluation entrypoints
deployment/    FastAPI serving stub, inference script
docker/        containerization
docs/          dataset / experiment / model-comparison reports (placeholders)
```

## License

MIT
