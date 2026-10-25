
import unittest, copy
from omega_v4 import *

class TestOmegaV4(unittest.TestCase):
    def test_irreversibility_bounds(self):
        X=[(0,0),(1,0),(0,0),(1,1),(0,1)]
        metric=RobustMetric().fit(X)
        core=OmegaCoreV4(metric=metric)
        for x in X:
            s=core.update(x)
            self.assertTrue(0<=s.irreversibility<=1)
            self.assertTrue(0<=s.path_efficiency<=1)

    def test_A_monotone(self):
        X=[(0,0),(1,2),(2,1),(1,1)]
        metric=RobustMetric().fit(X)
        core=OmegaCoreV4(metric=metric)
        prev=-1
        for x in X:
            s=core.update(x)
            self.assertGreaterEqual(s.A_global,prev)
            prev=s.A_global

    def test_metric_dimensionless(self):
        X=[(0,0),(100,1),(200,2)]
        m=RobustMetric().fit(X)
        self.assertEqual(len(m.scales),2)

if __name__=="__main__":
    unittest.main()
