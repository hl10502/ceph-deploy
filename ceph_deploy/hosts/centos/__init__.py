from . import mon  # noqa
from .install import install, mirror_install, repo_install, repository_url_part, rpm_dist  # noqa
from .uninstall import uninstall  # noqa
from ceph_deploy.util import pkg_managers
from ceph_deploy.util.system import is_systemd

# Allow to set some information about this distro
#

distro = None
release = None
codename = None


def choose_init(module):
    """
    Select a init system

    Returns the name of a init system (upstart, sysvinit ...).
    """

    # 兼容XenServer/WinServer，由于WinServer的major版本号<7，基于CentOS7.2，所以首先判断is_systemd
    if is_systemd(module.conn):
        return 'systemd'

    if module.normalized_release.int_major < 7:
        return 'sysvinit'

    if not module.conn.remote_module.path_exists("/usr/lib/systemd/system/ceph.target"):
        return 'sysvinit'

    return 'systemd'

def get_packager(module):
    return pkg_managers.Yum(module)
