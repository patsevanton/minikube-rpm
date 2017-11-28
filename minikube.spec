Name: minikube
Version: 0.23.0
Release: 1%{?dist}
Summary: Run Kubernetes locally

Group: Development Tools
URL: https://github.com/kubernetes/minikube
License: ASL 2.0
Source0: https://github.com/kubernetes/minikube/archive/v0.23.0.tar.gz

BuildRequires: gcc-go
#Requires:

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

