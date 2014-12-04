# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import os
import subprocess
import testtools

import heat_cfnclient

basepath = os.path.join(heat_cfnclient.__path__[0], os.path.pardir)


class CliTest(testtools.TestCase):
    def test_heat_cfn(self):
        self.bin_run('heat-cfn')

    def test_heat_boto(self):
        self.bin_run('heat-boto')

    def test_heat_watch(self):
        self.bin_run('heat-watch')

    def bin_run(self, bin):
        fullpath = basepath + '/bin/' + bin

        proc = subprocess.Popen(fullpath,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        if proc.returncode:
            print('Error executing %s:\n %s %s ' % (bin, stdout, stderr))
            raise subprocess.CalledProcessError(proc.returncode, bin)
