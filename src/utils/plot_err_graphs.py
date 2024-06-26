import pandas as pd
import matplotlib.pyplot as plt


def plot_err_graphs(repo_to_plot_from: str, output_name: str) -> None:

    plain18_df = pd.read_csv(
        "CIFAR_RESNET/results/performance_metrics/training_validation_acc.csv",
    )
    plain34_df = pd.read_csv(
        f"CIFAR_RESNET/results/performance_metrics/{repo_to_plot_from}/plain34/training_validation_acc.csv",
    )
    resnet18_df = pd.read_csv(
        f"CIFAR_RESNET/results/performance_metrics/{repo_to_plot_from}/resnet18/training_validation_acc.csv",
    )
    resnet34_df = pd.read_csv(
        f"CIFAR_RESNET/results/performance_metrics/{repo_to_plot_from}/resnet34/training_validation_acc.csv",
    )
    resnet50_df = pd.read_csv(
        f"CIFAR_RESNET/results/performance_metrics/{repo_to_plot_from}/resnet50/training_validation_acc.csv",
    )
    err_plain18_df = pd.DataFrame(
        {
            "Iterations": plain18_df["Epochs"] * 391,
            "TrainingErrorRate": 100 - plain18_df["TrainingAccuracy"],
            "ValidationErrorRate": 100 - plain18_df["ValidationAccuracy"],
        }
    )
    err_plain34_df = pd.DataFrame(
        {
            "Iterations": plain34_df["Epochs"] * 391,
            "TrainingErrorRate": 100 - plain34_df["TrainingAccuracy"],
            "ValidationErrorRate": 100 - plain34_df["ValidationAccuracy"],
        }
    )
    err_resnet18_df = pd.DataFrame(
        {
            "Iterations": resnet18_df["Epochs"] * 391,
            "TrainingErrorRate": 100 - resnet18_df["TrainingAccuracy"],
            "ValidationErrorRate": 100 - resnet18_df["ValidationAccuracy"],
        }
    )
    err_resnet34_df = pd.DataFrame(
        {
            "Iterations": resnet34_df["Epochs"] * 391,
            "TrainingErrorRate": 100 - resnet34_df["TrainingAccuracy"],
            "ValidationErrorRate": 100 - resnet34_df["ValidationAccuracy"],
        }
    )
    err_resnet50_df = pd.DataFrame(
        {
            "Iterations": resnet50_df["Epochs"] * 391,
            "TrainingErrorRate": 100 - resnet50_df["TrainingAccuracy"],
            "ValidationErrorRate": 100 - resnet50_df["ValidationAccuracy"],
        }
    )

    plt.figure(figsize=(10, 6))

    data_columns = [col for col in err_plain18_df.columns if col != "Iterations"]

    for data_column in data_columns:
        line_thickness = 1

        if data_column == "ValidationErrorRate":
            line_thickness = 2
        # plt.plot(
        #     err_plain34_df["Iterations"],
        #     err_plain34_df[data_column],
        #     label=data_column + " Plain34",
        #     linewidth=line_thickness,
        # )
        plt.plot(
            err_plain18_df["Iterations"],
            err_plain18_df[data_column],
            label=data_column + " Plain18",
            linewidth=line_thickness,
        )
        # plt.plot(
        #     err_resnet18_df["Iterations"],
        #     err_resnet18_df[data_column],
        #     label=data_column + " Resnet18",
        #     linewidth=line_thickness,
        # )
        # plt.plot(
        #     err_resnet34_df["Iterations"],
        #     err_resnet34_df[data_column],
        #     label=data_column + " Resnet34",
        #     linewidth=line_thickness,
        # )
        # plt.plot(
        #     err_resnet50_df["Iterations"],
        #     err_resnet50_df[data_column],
        #     label=data_column + " Resnet50",
        #     linewidth=line_thickness,
        # )

    plt.title("CIFAR-10 Error Rate Over Time")
    plt.xlabel("Iterations")
    plt.ylabel("Values")
    plt.legend()
    # plt.show()

    plt.savefig(f"/CIFAR_RESNET/{output_name}.png")


if __name__ == "__main__":
    plot_err_graphs("cifar", "for_reddit_only_plain")
