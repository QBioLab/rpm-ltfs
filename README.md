# rpm-ltfs
Spec files for LTFS

# Prereqsite

* Packages required for building LTFS
* rpmbuild
* spectool

# How to create rpm

1. Install rpmbuild `zypper install rpmbuild`
2. Install spectool `zypper install rpmdevtools`
3. Create rpmbuild directory structure if it is not existed `touch ./dummy.spec; rpmbuild ./dummy.spec`
4. copy ltfs.spec to rpmbuild/SPECS
5. cd rpmbuild
6. spectool -D -g -R ./SPECS/ltfs.spec
7. cd SPECS
8. rpmbuild -bs ltfs.spec
9. rpmbuild --rebuild ../SRPM/ltfs-2.4.2.0-10418.src.rpm

# Confimed OS

* Opensuse 15.1: ltfs.spec
