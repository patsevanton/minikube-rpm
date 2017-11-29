Name: minikube
Version: 0.23.0
Release: 1%{?dist}
Summary: Run Kubernetes locally

Group: Development Tools
URL: https://github.com/kubernetes/minikube
License: ASL 2.0
#Source0: https://github.com/kubernetes/minikube/archive/v0.23.0.tar.gz

BuildRequires: gcc-go
BuildRequires: git
BuildRequires: glibc-static
#Requires:

%description


%prep
#%setup -q
git clone https://github.com/kubernetes/minikube.git $GOPATH/src/k8s.io/minikube
cd $GOPATH/src/k8s.io/minikube

%build
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

