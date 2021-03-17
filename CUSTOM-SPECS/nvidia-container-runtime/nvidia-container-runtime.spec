Name: nvidia-container-runtime
Version: 3.4.2
Release: 2
Group: Development Tools

Vendor: NVIDIA CORPORATION
Packager: NVIDIA CORPORATION <cudatools@nvidia.com>

Summary: NVIDIA container runtime
URL: https://github.com/NVIDIA/nvidia-container-runtime
# runc NOTICE file: https://github.com/opencontainers/runc/blob/master/NOTICE
License: ASL 2.0

Source0: https://github.com/NVIDIA/nvidia-container-runtime/archive/v%{version}.tar.gz

BuildRequires: golang
Obsoletes: nvidia-container-runtime < 2.0.0
Requires: nvidia-container-toolkit >= 1.4.2, nvidia-container-toolkit < 2.0.0

%if 0%{?suse_version}
Requires: libseccomp2
Requires: libapparmor1
%else
Requires: libseccomp
%endif

%description
Provides a modified version of runc allowing users to run GPU enabled
containers.

%prep
%setup -q

%build
export GO_BUILD_DIR=go/src/gitlab.com/nvidia/container-toolkit/nvidia-container-runtime
mkdir -p $GO_BUILD_DIR
cp -r src/* $GO_BUILD_DIR
pushd $GO_BUILD_DIR
make build
popd
mv $GO_BUILD_DIR/nvidia-container-runtime .

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} nvidia-container-runtime

%files
%license LICENSE
%{_bindir}/nvidia-container-runtime

%changelog
* Wed Mar 17 2021 MICROSOFT(via BEYONDSOFT) <v-arthurlai@microsoft.com> 3.4.2-1
- Bump 3.4.2-1 to 3.4.2-2
- Integrate into CBL-Mariner RPM build system

* Fri Feb 05 2021 NVIDIA CORPORATION <cudatools@nvidia.com> 3.4.2-1
- Add dependence on nvidia-container-toolkit >= 1.4.2

* Mon Jan 25 2021 NVIDIA CORPORATION <cudatools@nvidia.com> 3.4.1-1
- Update README to list 'compute' as part of the default capabilities
- Switch to gomod for vendoring
- Update to Go 1.15.6 for builds
- Add dependence on nvidia-container-toolkit >= 1.4.1

* Wed Sep 16 2020 NVIDIA CORPORATION <cudatools@nvidia.com> 3.4.0-1
- Bump version to v3.4.0
- Add dependence on nvidia-container-toolkit >= 1.3.0

* Wed Jul 08 2020 NVIDIA CORPORATION <cudatools@nvidia.com> 3.3.0-1
- e550cb15 Update package license to match source license
- f02eef53 Update project License
- c0fe8aae Update dependence on nvidia-container-toolkit to 1.2.0

* Fri May 15 2020 NVIDIA CORPORATION <cudatools@nvidia.com> 3.2.0-1
- e486a70e Update build system to support multi-arch builds
- 854f4c48 Require new MIG changes
