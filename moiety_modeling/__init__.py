#!/usr/bin/python3
# -*- coding: utf-8 _*_

"""
The moiety_modeling API Reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Routines for working with moiety modeling.

This package includes the following modules:

``modeling``
    This module provides the :class:`~moiety_modeling.modeling.Dataset` class to organize a single mass spectroscopy
    profile dataset into a dictionary-based data structure, and the :class:`~moiety_modeling.modeling.OptimizationManager`
    class to manage the optimization process of moiety modeling.

``cli``
    This module provides command-line interface for the ``moiety_modeling`` package.


``model``
    This module provides the :class:`~moiety_modeling.model.Moiety` class, the :class:`~moiety_modeling.model.Molecule`
    class, the :class:`~moiety_modeling.model.Relationship` class, and the :class:`~moiety_modeling.model.Model`
    class to construct moiety model.

``analysis``
    This module provides several classes to analyze the optimization results, select the optimal model, and visualize the
    results. The :class:`~moiety_modeling.analysis.ResultAnalysis` class is responsible for generating general statistics
    from the optimization results. The :class:`~moiety_modeling.analysis.ModelRank` class selects the model that best
    reflects the observed isotopologue profile. The :class:`~moiety_modeling.analysis.ComparisonTable` class compares
    the optimal model selected under different optimization settings. The :class:`~moiety_modeling.analysis.PlotMoietyDistribution`
    class plots the distribution of moiety value of the moiety model. The :class:`~moiety_modeling.analysis.PlotIsotopologueIntensity`
    class plots comparison of the observed and the calculated isotopologue intensity.

"""

__version__ = "1.0"

from .modeling import *
from .model import *

