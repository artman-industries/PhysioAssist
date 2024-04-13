import numpy as np
import sys
sys.path.append('..')
from infra.generation_functions import *
import plotly.graph_objects as go
import os


def run_threshold_experiment(good_reps, bad_reps, performance_evaluation_function, threshold_range, model_name, show_fig=True):
    """
    Run an experiment to evaluate squat performance using a given performance evaluation function
    and a range of thresholds.

    Parameters:
    - performance_evaluation_function: A function that evaluates squat performance for a given repetition.
    - threshold_range: A list or array containing the range of thresholds to be evaluated.
    - show_fig: Boolean indicating whether to display the Plotly figure (default is True).

    Returns:
    - A list of dictionaries containing evaluation metrics for each threshold.

    Evaluation Metrics:
    - Threshold: The threshold value used for evaluation.
    - TPR (True Positive Rate): The ratio of true positives to the total actual positives.
    - FPR (False Positive Rate): The ratio of false positives to the total actual negatives.
    - TNR (True Negative Rate): The ratio of true negatives to the total actual negatives.
    - FNR (False Negative Rate): The ratio of false negatives to the total actual positives.
    - Precision: The ratio of true positives to the total predicted positives.
    - Recall: The ratio of true positives to the total actual positives.
    - F1 Score: The harmonic mean of precision and recall.

    If show_fig is True, two Plotly figures are created and displayed:
    - The first figure shows F1 score, precision, and recall against the threshold values.
    - The second figure shows the number of correct predictions against the threshold values.
    # """
    # Evaluate performance for good and bad squats
    good_squats_performance = [performance_evaluation_function(rep) for rep in good_reps]
    bad_squats_performance = [performance_evaluation_function(rep) for rep in bad_reps]


    # List to store results for each threshold
    results_list = []

    # List to store correct predictions for each threshold
    correct_predictions_list = []

    # Analyze performance for different thresholds
    for threshold in threshold_range:
        # Count the number of true positive, false positive, true negative, and false negative
        true_positive = sum(
            1 if sum(np.where(array <= threshold, 1, 0)) >= len(array)/2 else 0
            for array in good_squats_performance)
        false_positive = sum(
            1 if sum(np.where(array <= threshold, 1, 0)) >= len(array)/2 else 0
            for array in bad_squats_performance)
        true_negative = sum(
            1 if sum(np.where(array > threshold, 1, 0)) > len(array)/2 else 0
            for array in bad_squats_performance)
        false_negative = sum(
            1 if sum(np.where(array > threshold, 1, 0)) > len(array)/2 else 0
            for array in good_squats_performance)
        print(f'threshold {threshold}:')
        print(f'{model_name=}')
        print(f'{true_positive=}')
        print(f'{false_positive=}')
        print(f'{true_negative=}')
        print(f'{false_negative=}')
        print('\n')
        # Calculate rates
        total_positive = true_positive + false_negative
        total_negative = true_negative + false_positive

        true_positive_rate = true_positive / total_positive if total_positive > 0 else 0
        false_positive_rate = false_positive / total_negative if total_negative > 0 else 0
        true_negative_rate = true_negative / total_negative if total_negative > 0 else 0
        false_negative_rate = false_negative / total_positive if total_positive > 0 else 0

        # Calculate F1 score
        precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
        recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        # Store results in a dictionary
        result_dict = {
            'Threshold': threshold,
            'TPR': true_positive_rate,
            'FPR': false_positive_rate,
            'TNR': true_negative_rate,
            'FNR': false_negative_rate,
            'correct_predictions': true_positive + true_negative,
            'Precision': precision,
            'Recall': recall,
            'F1 Score': f1_score,
        }

        results_list.append(result_dict)

        # Count the total correct predictions
        total_correct_predictions = true_positive + true_negative
        correct_predictions_list.append(total_correct_predictions)

    if show_fig:
        # Extract data for plotting
        thresholds = [result['Threshold'] for result in results_list]
        f1_scores = [result['F1 Score'] for result in results_list]
        precision = [result['Precision'] for result in results_list]
        recall = [result['Recall'] for result in results_list]
        true_positive_rate = [result['TPR'] for result in results_list]
        false_negative_rate = [result['FNR'] for result in results_list]

        # Create the first Plotly figure (F1 score, precision, and recall)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=thresholds, y=f1_scores, mode='lines', name='F1 Score'))
        fig1.add_trace(go.Scatter(x=thresholds, y=precision, mode='lines', name='Precision'))
        fig1.add_trace(go.Scatter(x=thresholds, y=recall, mode='lines', name='Recall'))
        fig1.update_layout(
            title='Evaluation Metrics vs. Threshold',
            xaxis_title='Threshold',
            yaxis_title='Score',
            legend=dict(x=0, y=1, traceorder='normal', orientation='h')
        )
                # Save the figure as HTML file
        html_file_path = "Evaluation_Metrics_vs_Threshold.html"
        fig1.write_html(html_file_path, auto_open=True)

        # Print the path to the HTML file
        print("Plotly graph saved as:", os.path.abspath(html_file_path))

        # Extract data for plotting correct predictions
        correct_predictions = correct_predictions_list

        # Create the second Plotly figure (Correct predictions)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=thresholds, y=correct_predictions, mode='lines', name='Correct Predictions'))
        fig2.update_layout(
            title='Correct Predictions vs. Threshold',
            xaxis_title='Threshold',
            yaxis_title='Correct Predictions',
        )
                # Save the figure as HTML file
        html_file_path = "Correct_Predictions_vs_Threshold.html"
        fig2.write_html(html_file_path, auto_open=True)

        # Print the path to the HTML file
        print("Plotly graph saved as:", os.path.abspath(html_file_path))

        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=thresholds, y=true_positive_rate, mode='lines', name='TPR'))
        fig3.add_trace(go.Scatter(x=thresholds, y=false_negative_rate, mode='lines', name='FNR'))

        fig3.update_layout(
            title='TPR & FNR vs. Threshold',
            xaxis_title='Threshold',
            yaxis_title='TPR & FNR ',
        )
        # Save the figure as HTML file
        html_file_path = "TPR&FNR_vs_Threshold.html"
        fig3.write_html(html_file_path, auto_open=True)

        # Print the path to the HTML file
        print("Plotly graph saved as:", os.path.abspath(html_file_path))

    return results_list
