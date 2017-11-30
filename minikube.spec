%global _prefix /usr/local

Name:    minikube
Version: 0.24.0
Release: 1%{?dist}
Summary: Run Kubernetes locally

Group:   Development Tools
URL:     https://github.com/kubernetes/minikube
License: ASL 2.0
Source0: https://storage.googleapis.com/minikube/releases/latest/%{name}-linux-amd64

%description

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

