Name: minikube
Version: 0.23.0
Release: 1%{?dist}
Summary: Run Kubernetes locally

Group: Development Tools
URL: https://github.com/kubernetes/minikube
License: ASL 2.0
Source0: https://github.com/kubernetes/minikube/releases/download/v0.23.0/minikube-linux-amd64

%description

%install
%{__rm} -rf %{buildroot}/*
mkdir -p %{buildroot}/usr/local/bin
cp -a %{_sourcedir}/minikube-linux-amd64 %{buildroot}/usr/local/bin

%files
%{buildroot}/usr/local/bin/minikube-linux-amd64
