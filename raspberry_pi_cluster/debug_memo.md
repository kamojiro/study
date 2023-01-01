# 

```bash
systemctl status kubelet
kubectl logs -n kube-system kube-flannel-ds-arm-vl44m
```

## Raspberry Pi

```bash
ubuntu@k8s-master:~$ uname -a
Linux k8s-master 5.15.0-1012-raspi #14-Ubuntu SMP PREEMPT Fri Jun 24 13:10:28 UTC 2022 aarch64 aarch64 aarch64 GNU/Linux
```

```bash
ubuntu@k8s-master:~$ crio --version
crio version 1.25.0
Version:        1.25.0
GitCommit:      5969b091d50192ce84fe0032777dafd98b4203d1
GitCommitDate:  2022-12-01T14:26:50Z
GitTreeState:   dirty
BuildDate:      1980-01-01T00:00:00Z
GoVersion:      go1.18.1
Compiler:       gc
Platform:       linux/arm64
Linkmode:       static
BuildTags:      
  static
  netgo
  osusergo
  exclude_graphdriver_btrfs
  exclude_graphdriver_devicemapper
  seccomp
  apparmor
  selinux
LDFlags:          -s -w -X github.com/cri-o/cri-o/internal/pkg/criocli.DefaultsPath="" -X github.com/cri-o/cri-o/internal/version.buildDate=1980-01-01T00:00:00Z -s -w -linkmode external -extldflags "-static -lm"
SeccompEnabled:   true
AppArmorEnabled:  false
Dependencies:     
  
ubuntu@k8s-master:~$ kubelet --version
Kubernetes v1.25.4

```