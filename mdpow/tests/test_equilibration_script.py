import mdpow.equil
import tempdir as td
import os
import manifest

class TestEquilibriumScript(object):
    
    def setup(self):
        self.tmpdir = td.TempDir()
        self.old_path = os.getcwd()
        self.resources = self.old_path + "/mdpow/tests/testing_resources"
        m = manifest.Manifest(os.path.join(self.resources,'manifest.yml'))
        m.assemble('base',self.tmpdir.name)

    def _run_equil(self, solvent, dirname):
        try:
            cfg = get_configuration(runfile)
            self.S = equilibrium_simulation(cfg, solvent, dirname=dirname)
        except:
            assert False

    def test_basic_run(self):
        _run_equil('water','benzene/')
