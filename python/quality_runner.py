__copyright__ = "Copyright 2016, Netflix, Inc."
__license__ = "Apache, Version 2.0"

import os
import multiprocessing
import subprocess
import config
from tools import get_dir_without_last_slash, make_parent_dirs_if_nonexist
from executor import Executor
from result import Result

class QualityRunner(Executor):
    """
    QualityRunner takes in a list of assets, and run feature extraction on
    them, and return a list of corresponding results. A QualityRunner must
    specify a unique type and version combination (by the TYPE and VERSION
    attribute), so that the Result generated by it can be identified.

    Two category of subclassing QualityRunners: 1) calling external quality
    metric (e.g. AWCY SSIM or FastSSIM) directly to get the quality scores.
    2) calling internal FeatureExtractor for features followed by calling
    internal TrainTestModels.predict().
    """

    def _read_result(self, asset):

        result = {}
        result.update(self._get_quality_scores(asset))
        return Result(asset, self.executor_id, result)

