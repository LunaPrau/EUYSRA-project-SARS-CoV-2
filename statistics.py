"""
Full script for extracting two variables from .csv files of //this format: //
and performing mean unsigned error, root mean square deviation,
Pearson's linear & Spearman's rank & Kendall's rank correlation coefficients.

Both mean unsigned error and root mean square deviation were alculated using the sklearn.metrics package.
Pearson's linear & Spearman's rank & Kendall's rank correlation coefficients were calculated using the scipy.stats package.

*!*!*! With reference to:
"Assessment of Binding Affinity via Alchemical Free Energy Calculations"
Maximilian Kuhn, Stuart Firth-Clark, Paolo Tosco, Antonia S.J.S. Mey, Mark Mackey, Julien Michel.
Analysis adapted from freenergyframework and a plotting example by Hannah Bruce McDonald:
https://github.com/choderalab/freeenergyframework/blob/master/freeenergyframework/examples/WhyNotToUseR2ForDDG.ipynb
"""

%pylab inline
import pandas as pd
import numpy as np
import sklearn.metrics
import scipy.stats
import copy
import os

sns.set_context("notebook", font_scale=1.2)

base_dir = ""

def compute_statistic(y_true_sample, y_pred_sample):
    """Compute requested statistic.

    Parameters
    ----------
    y_true : ndarray with shape (N,)
        True values
    y_pred : ndarray with shape (N,)
        Predicted values
    statistic : str
        Statistic, one of ['RMSE', 'MUE', 'R2', 'rho']

    """
    RMSE = np.sqrt(sklearn.metrics.mean_squared_error(y_true_sample, y_pred_sample))
    MUE = sklearn.metrics.mean_absolute_error(y_true_sample, y_pred_sample)
    _, _, r_value, _, _ = scipy.stats.linregress(y_true_sample, y_pred_sample)
    rho = scipy.stats.pearsonr(y_true_sample, y_pred_sample)[0]
    tau = scipy.stats.kendalltau(y_true_sample, y_pred_sample)[0]
    return RMSE, MUE, r_value, rho, tau

def plotting_data(x, y, x_label, y_label, error=None):
    fig = figure(figsize=(6,6))
    omax = -15
    omin = 5
    plt.scatter(x,y, marker='o')
    plt.axis([omax, omin, omax, omin])
    plt.xticks(np.arange(omax-1, omin+2, 2))
    plt.yticks(np.arange(omax-1, omin+2, 2))
    RMSE, MUE, r_value, rho, tau = compute_statistic(x,y)
    plt.title(f'RMSE:{RMSE:.2}, MUE:{MUE:.2}, R:{r_value:.2}, rho:{rho:.2}, tau:{tau:.2}')
    plt.xlabel(x_label+' $\delta$G [kcal/mol]')
    plt.ylabel(y_label+' $\delta$G [kcal/mol]')
    plt.savefig(base_dir+"-"+x_label+"-"+y_label+".png", facecolor='white', transparent=False, dpi=199, bbox_inches='tight')

def extract_A_B(name_A, name_B, base_dir=base_dir):
    computed_data_name = os.path.join(base_dir,name_A,'dG.csv')
    experi_data_name = os.path.join(base_dir,name_B,'dG.csv')
    computed_df = pd.read_csv(computed_data_name,comment='#')
    computed_df.Ligand_Name = computed_df.Ligand_Name.astype(str)
    computed_df.Site_Number = computed_df.Site_Number.astype(str)
    computed_df.With_Or_Without_Water = computed_df.With_Or_Without_Water.astype(str)

    experi_df = pd.read_csv(experi_data_name)
    experi_df.Ligand_Name = computed_df.Ligand_Name.astype(str)
    experi_df.Site_Number = computed_df.Site_Number.astype(str)
    experi_df.With_Or_Without_Water = computed_df.With_Or_Without_Water.astype(str)

    computed = []
    experiment = []
    
    i = 0
    j = 0
    while i < computed_df.shape[0] :     
        while j < experi_df.shape[0] and i < computed_df.shape[0]:
            if computed_df.at[ i,'Ligand_Name' ] == experi_df.at[ j, 'Ligand_Name' ]:
                computed.append( computed_df.at[ i,'Mean' ] )
                experiment.append( experi_df.at[ j,'Mean' ] )
                i += 1
            j += 1          
        i += 1
    
    return experiment, computed
	
# Flare vs. AutoDock
name_A='Flare'
name_B='AutoDock'
X,Y = extract_A_B(name_A,name_B)
plotting_data(X,Y,name_A,name_B)

# Flare vs. rDock
name_A_WOW='Flare_WOW'
name_A='Flare'
name_B='rDock'
X,Y = extract_A_B(name_A_WOW,name_B)
plotting_data(X,Y,name_A,name_B)

# AutoDock vs. rDock
name_A_WOW='AutoDock_WOW'
name_A='AutoDock'
name_B='rDock'
X,Y = extract_A_B(name_A_WOW,name_B)
plotting_data(X,Y,name_A,name_B)