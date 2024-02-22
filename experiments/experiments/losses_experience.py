import numpy as np

from experiments.experiments.threshold_experiment import run_threshold_experiment
from experiments.infra.generation_functions import *
import plotly.graph_objects as go


def run_losses_experiment(good_reps, bad_reps, performance_evaluation_functions_list: list, threshold_list: list,
                          show_fig=True):
    assert len(performance_evaluation_functions_list) == len(threshold_list)
    reps_performances = [
        run_threshold_experiment(good_reps, bad_reps, performance_evaluation_function, [threshold], show_fig=False)[0]
        for
        threshold, performance_evaluation_function in
        zip(threshold_list, performance_evaluation_functions_list)]

    if show_fig:
        # Extract data for plotting
        thresholds = [result['Threshold'] for result in reps_performances]
        f1_scores = [result['F1 Score'] for result in reps_performances]
        precision = [result['Precision'] for result in reps_performances]
        recall = [result['Recall'] for result in reps_performances]

        # List to store correct predictions for each threshold
        correct_predictions_list = [result['TPR'] + result['TNR'] for result in reps_performances]

        # # Create the first Plotly figure (F1 score, precision, and recall)
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
        # fig1.show()

        # Create the second Plotly figure (Correct predictions)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=list(range(len(threshold_list))), y=correct_predictions_list, mode='lines', name='Correct Predictions'))
        fig2.update_layout(
            title='Correct Predictions vs. model number',
            xaxis_title='model number',
            yaxis_title='Correct Predictions',
        )
        fig2.show()
