import tempdir as td
import os
import manifest

from mdpow.run import fep_simulation
from mdpow.config import get_configuration

class TestFEPScript(object):
    
    def setup(self):
        self.tmpdir = td.TempDir()
        self.old_path = os.getcwd()
        self.resources = self.old_path + "/mdpow/tests/testing_resources"
        m = manifest.Manifest(os.path.join(self.resources,'manifest.yml'))
        m.assemble('md_npt',self.tmpdir.name)

    def _run_fep(self, solvent, dirname):
        try:
            cfg = get_configuration('runinput.yml')
            self.S = fep_simulation(cfg, solvent, dirname=dirname)
        except:
            assert False

    def test_basic_run(self):
        os.chdir(self.tmpdir.name)
        try:
            self._run_fep('water','benzene/')
        except:
            assert False
        finally:
            os.chdir(self.old_path)
