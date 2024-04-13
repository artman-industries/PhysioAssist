import numpy as np
import sys
sys.path.append('..')
import os
from experiments.threshold_experiment import run_threshold_experiment
from infra.generation_functions import *
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def run_losses_experiment(good_reps, bad_reps, performance_evaluation_functions_list: list, threshold_list: list, models_names: list, 
                          show_fig=True):
    assert len(performance_evaluation_functions_list) == len(threshold_list)
    reps_performances = [
        run_threshold_experiment(good_reps, bad_reps, performance_evaluation_function, [threshold], model_name, show_fig=False)[0]
        for
        threshold, performance_evaluation_function, model_name in
        zip(threshold_list, performance_evaluation_functions_list, models_names)]

    if show_fig:
        # Extract data for plotting
        thresholds = [result['Threshold'] for result in reps_performances]
        f1_scores = [result['F1 Score'] for result in reps_performances]
        precision = [result['Precision'] for result in reps_performances]
        recall = [result['Recall'] for result in reps_performances]

        # List to store correct predictions for each threshold
        correct_predictions_list = [result['correct_predictions'] for result in reps_performances]

        # Create the first Plotly figure (F1 score, precision, and recall)
        # fig1 = go.Figure()
        # fig1.add_trace(go.Scatter(x=thresholds, y=f1_scores, mode='lines', name='F1 Score'))
        # fig1.add_trace(go.Scatter(x=thresholds, y=precision, mode='lines', name='Precision'))
        # fig1.add_trace(go.Scatter(x=thresholds, y=recall, mode='lines', name='Recall'))
        # fig1.update_layout(
        #     title='Evaluation Metrics vs. Threshold',
        #     xaxis_title='Threshold',
        #     yaxis_title='Score',
        #     legend=dict(x=0, y=1, traceorder='normal', orientation='h')
        # )
        # # Save the figure as HTML file
        # html_file_path = "first_experiment_Evaluation Metrics.html"
        # fig1.write_html(html_file_path, auto_open=True)

        # # Print the path to the HTML file
        # print("Plotly graph saved as:", os.path.abspath(html_file_path))

        # Define the model names and their performance metrics
        metrics = {
            "Precision": [result['Precision'] for result in reps_performances],
            "Recall": [result['Recall'] for result in reps_performances],
            "F1 Score": [result['F1 Score'] for result in reps_performances],
        }

        # Plot each metric for each model
        fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 16), sharex=True, gridspec_kw={'hspace': 0.5})
        for i, (metric, values) in enumerate(metrics.items()):
            ax = axes[i]
            ax.bar(models_names, values)
            ax.set_title(metric)
            ax.set_ylabel(metric)

        plt.tight_layout()
        plt.show()


        # Create the second Plotly figure (Correct predictions)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=models_names, y=correct_predictions_list, mode='lines', name='Correct Predictions'))
        fig2.update_layout(
            title='Correct Predictions vs. model number',
            xaxis_title='model number',
            yaxis_title='Correct Predictions',
        )
        # Save the figure as HTML file
        html_file_path = "first_experiment_correct_predictions.html"
        fig2.write_html(html_file_path, auto_open=True)

        # Print the path to the HTML file
        print("Plotly graph saved as:", os.path.abspath(html_file_path))
