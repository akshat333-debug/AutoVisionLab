def generate_report(results):

    report = "# Experiment Results\n\n"

    for model, score in results.items():

        report += f"{model}: {score}\n"

    with open("docs/experiment_results.md","w") as f:
        f.write(report)