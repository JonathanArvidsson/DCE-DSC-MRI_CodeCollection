from src.original.T1_mapping.McGill.vfa import despot, novifast
import pytest
import numpy as np

# Test for specific inputs and expected outputs :
"""
For the time being, simulated values without noise have been specified to test the fit.
Additional test cases with varying degrees of noise should be included, from maybe a DRO.
"""
    
@pytest.mark.parametrize('S_t, fa_array, tr_S, T1_est, S0', [(np.array([48.86,58.95,69.14,63.22]),np.array([20,15,10,5]),0.01,1.,1000.)])
def test_fit_vfa_despot(S_t, fa_array, tr_S, T1_est, S0):
    fa_array_rad = np.deg2rad(fa_array)
    np.testing.assert_array_almost_equal(despot(S_t, fa_array_rad, tr_S), [S0, T1_est], decimal=2)

@pytest.mark.parametrize('S_t, fa_array, tr_S, T1_est, S0', [(np.array([48.86,58.95,69.14,63.22]),np.array([20,15,10,5]),0.01,1.,1000.)])
def test_fit_vfa_novifast(S_t, fa_array, tr_S, T1_est, S0):
    fa_array_rad = np.deg2rad(fa_array)
    np.testing.assert_array_almost_equal(novifast(S_t, fa_array_rad, tr_S), [[S0],[T1_est]], decimal=2)

@pytest.mark.parametrize('S_t, fa_array, tr_S, T1_est, S0', [(np.array([48.86,58.95,69.14,63.22]),np.array([20,15,10,5]),0.01,1.,1000.)])
def test_fit_vfa_novifast_noninterative(S_t,fa_array, tr_S, T1_est, S0):
    fa_array_rad = np.deg2rad(fa_array)
    np.testing.assert_array_almost_equal(np.round(novifast(S_t, fa_array_rad, tr_S, doiterative=False)),[[S0],[T1_est]],decimal=2)
